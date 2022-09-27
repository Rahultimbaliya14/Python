from codecs import oem_decode
from email.mime import audio
import pyautogui as a
import pyttsx3
import speech_recognition as sr 
import time as t
#for press two key
# a.keyDown("alt")
# a.keyDown("f4")
# t.sleep(0.5)
# a.keyUp("alt")
# a.keyUp("f4")
# a.hotkey("alt","f4")

#for move cursor
# a.moveTo(139,229,duration=2)


#for Take Screen Screen Shot
# img=a.screenshot()
# img.show()



a.press("win")
t.sleep(1)
a.write("crome", interval=0.20)
a.press("enter")
t.sleep(2)
a.write("github",interval=0.10)
a.press("f11")
# for i in range(10):
#     a.press("f11")
#     a.press("f5")
#     t.sleep(0.5)
# a.alert("Welcome To My Program do  not click The Cancel Button")
# t.sleep(1)
# a.press("up")
# a.write("")
# a.press("enter")
# t.sleep(2)
# a.hotkey("ctrl","z")
# a.alert("Work Is Over You Want To Exit")

# engine=pyttsx3.init()
# engine.say("my first program to say")
# engine.say("my first program to ghare")
# engine.say("My Name Is Rahul  and Iam Study On the Bca Computer Science")
 








def main():
    import pyautogui as a
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say somethin")
        audio=r.listen(source)

        try:
            a=str(r.recognize_google(audio))
            print(a)
            print("you said : \n "+r.recognize_google(audio))
        
            if(a=="hello"):
                engine.say("yes sir")
                engine.runAndWait()
                a.p("enter")
                  
            

        except Exception as e:
            print(e)
        

        with open("recorgnise.wav","wb") as f:
            f.write(audio.get_wav_data())

if __name__=="__main__":
    main()