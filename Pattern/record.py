import pyautogui as a
import pyttsx3
import speech_recognition as sr 
import time as t
import pywhatkit as play
i=0
# while i<=10:
#      play.sendwhatmsg_instantly("+916353647592","helo",tab_close=True)
#      i+=1
def main():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        import pyttsx3
        r.adjust_for_ambient_noise(source)
        engine1=engine=pyttsx3.init()
        engine1.say("Welcome Sir What Can Do For You")
        engine1.runAndWait()
        print("listening")
        audio=r.listen(source)

        try:
            import pyautogui as a
            import pyttsx3
            engine=engine=pyttsx3.init()
            b=str(r.recognize_google(audio))
            b=b.lower()
            print(b)

            print(b)
            print("you said : \n "+r.recognize_google(audio))
            if(b=="open file"):
                import pyautogui as a
                engine.say("yes sir Opening File Explorer")
                engine.runAndWait()
                a.hotkey("win","e")
            elif(b=="open chrome"):
                import pyautogui as a
                engine.say("yes sir Opening Crome Browser")
                engine.runAndWait()
                a.press("win")
                t.sleep(0.25)
                a.write("crome",interval=0.10)
                a.press("enter")
            elif(b=="shutdown"):
                import pyautogui as a
                engine.say("ok sir shutdown Your Pc in 2 seconds")
                engine.runAndWait()
                t.sleep(4)
                a.hotkey("ctrl","f4")
            elif('play' in b):
                engine.say("Ok Sir"+b)
                engine.runAndWait()
                print(b)
                play.playonyt(b)
            else:
                engine.say("This Can Find On The Web")
                engine.runAndWait()
                play.search(b)
        except Exception as e:
            print(e)

  
if __name__=="__main__":
    main()