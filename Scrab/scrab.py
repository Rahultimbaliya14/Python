import requests
import threading
import os
import time
from bs4 import BeautifulSoup
import re
from PIL import Image
from reportlab.pdfgen import canvas
from playwright.sync_api import sync_playwright

examname ="pl-300" # User Input (name in small like az-104)
totalQu = 334 # User Input grab from the site

loading = True

def show_loading():
    i = 0
    while loading:
        dots = '.' * (i % 10 + 1)
        print(f"\rLoading{dots:<10}", end='', flush=True)
        time.sleep(0.3)
        i += 1
    print("\r" + " " * 20 + "\r", end='', flush=True)

t = threading.Thread(target=show_loading)
t.start()

finndedQue = 0
i = 1
while finndedQue < totalQu :
    url = "https://www.examtopics.com/discussions/microsoft/"+str(i)+"/" 
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch the page, status code: {response.status_code}")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.find_all('a', href=True)

        find_links = [link['href'] for link in links if examname in link['href']]

        with open(examname+'_links.txt', 'a') as file:
            for pl_link in find_links:
                finndedQue +=1
                file.write("https://www.examtopics.com"+pl_link + '\n')
    i = i+1

loading = False
t.join()

print("Grab Complate ........")

#sort 
with open(examname+'_links.txt', 'r') as file:
    urls = file.read().splitlines()

def extract_topic_question(url):
    match = re.search(r'topic-(\d+)-question-(\d+)', url)
    if match:
        topic = int(match.group(1))
        question = int(match.group(2))
        return (topic, question)
    return (float('inf'), float('inf')) 

sorted_urls = sorted(urls, key=extract_topic_question)
with open(examname+'_links_sort.txt', 'a') as filesort:
    for url in sorted_urls:
        filesort.write(url + '\n')

print("Sorting Complate ........")

# Ensure screenshot directory exists
os.makedirs(examname+"_screenshot", exist_ok=True)

# Read URLs from file
with open(examname+'_links_sort.txt', 'r') as f:
    urls = [line.strip() for line in f if line.strip()]

# Take screenshots
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    
    for idx, url in enumerate(urls):
        page = context.new_page()
        page.goto(url)

        try:
            page.evaluate('''() => {
                const nav = document.querySelector('div.action-row-container');
                if (nav) nav.remove();
            }''')
            page.evaluate('''() => {
                const nav = document.querySelector('div.footer-top');
                if (nav) nav.remove();
            }''')
            page.evaluate('''() => {
                const nav = document.querySelector('div.footer-bottom');
                if (nav) nav.remove();
            }''')
            page.evaluate('''() => {
                const nav = document.querySelector('div.contrib__ulimited');
                if (nav) nav.remove();
            }''')
            page.evaluate('''() => {
                const nav = document.querySelector('div.rs-toolbar');
                if (nav) nav.remove();
            }''')

            page.evaluate('''() => {
                const nav = document.querySelector('header.rs-header');
                if (nav) nav.remove();
            }''')

            page.evaluate('''() => {
                const nav = document.querySelector('div.col-sm-12');
                if (nav) nav.remove();
            }''')

            page.evaluate('''() => {
                const nav = document.querySelector('div.discussion-page-comments-section');
                if (nav) nav.remove();
            }''')
            
            page.wait_for_selector('a.btn.btn-primary.reveal-solution', timeout=5000)
            page.click('a.btn.btn-primary.reveal-solution')
            page.wait_for_timeout(2000)  
        except Exception as e:
            print(f"Clickable element not found or failed on {url}: {e}")

        # Take screenshot
        screenshot_path = os.path.join(examname+"_screenshot", f'screen_{idx+1}.png')
        page.screenshot(path=screenshot_path, full_page=True)
        page.close()

    browser.close()
print("Taked All the Screenshot ........")

with open(examname+'_links_sort.txt', 'r') as f:
    urls = [line.strip() for line in f if line.strip()]
c = canvas.Canvas(examname+"_dumps.pdf")
for idx in range(len(urls)):
    img_path = os.path.join(examname+"_screenshot", f'screen_{idx+1}.png')
    image = Image.open(img_path)
    width, height = image.size
    c.setPageSize((width, height))
    c.drawImage(str(img_path), 0, 0, width=width, height=height)
    c.showPage()
c.save()

for idx in range(len(urls)):
    img_path = examname+"_screenshot"  f'screenshot_{idx+1}.png'
    if img_path.exists():
        img_path.unlink()

