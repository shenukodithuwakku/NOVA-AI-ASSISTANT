import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
from time import sleep

listener=sr.Recognizer()
engine=pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('\nListening...')
            voice=listener.listen(source)
            info=listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        talk("Sorry , Did not understand the audio.") 
        pass

def whatsappmsg(name,message,time_hour,time_min):

    kt.sendwhatmsg(name,message,time_hour,time_min)

number_list = {
    "Amma": "+94782511654",
    "Thaththa": "+94771234567",
    "Friend": "+94770000000"
}

def writemsg():
    talk("to whom you want to send whatsapp")
    print("towhom you want to send whatsapp")
    name=get_info()
    if name in number_list:
        name = number_list[name]
    else:
        talk("Name not found in contact list.")
        return
    print(name)
    talk("what is message who you want to send")
    print("what is message who you want to send")
    message=get_info()
    print(message)
    talk("what time do you want to send message")
    time_hour=get_info()
    time_hour=int(time_hour)
    time_min=get_info()
    time_min=int(time_min)
    print(float(time_hour),":",float(time_min))
    whatsappmsg(name,message,time_hour,time_min)
    print("Whatsapp message has been sent successfully!!")

    talk("Whatsapp message has been sent successfully!!")
    talk("Do you want to send more messages")
    send_more=get_info()
    if "yes" in send_more.lower():
        writemsg()

writemsg()


