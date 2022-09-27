import pyautogui as a
import pyttsx3
import speech_recognition as sr 
import time as t
def main():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say somethin")
        audio=r.listen(source)

        try:
            import pyautogui as a
            import pyttsx3
            engine=engine=pyttsx3.init()
            a=str(r.recognize_google(audio))
            print(a)
            print("you said : \n "+r.recognize_google(audio))
            if(a=="open file"):
                import pyautogui as a
                engine.say("yes sir Opening File Explorer")
                engine.runAndWait()
                a.hotkey("win","e")
            elif(a=="open Chrome"):
                import pyautogui as a
                engine.say("yes sir Opening Crome Browser")
                engine.runAndWait()
                a.press("win")
                t.sleep(0.25)
                a.write("crome",interval=0.10)
                a.press("enter")
            elif(a=="shutdown"):
                import pyautogui as a
                engine.say("ok sir shutdown Your Pc in 2 seconds")
                engine.runAndWait()
                t.sleep(4)
                a.hotkey("ctrl","f4")


        except Exception as e:
            print(e)
        

        with open("recorgnise.wav","wb") as f:
            f.write(audio.get_wav_data())

if __name__=="__main__":
    main()