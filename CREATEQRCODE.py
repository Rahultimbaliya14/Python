import pyqrcode
import png
from pyqrcode import QRCode
link=input("Paste Your Link To Generate QRCode:")
url=pyqrcode.create(link)
url.svg("ny.svg",scale=8)
url.png("my.png" ,scale=6)
