from os import startfile
from tracemalloc import start
from xnl.etree.ElementTree import fromstring
import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
from item import sleep
import getpass as gp

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

number_list = {"Amma":"0782511654"}

def writemsg():
    talk("to whom you want to send whatsapp")
    print("towhom you want to send whatsapp")
    name=get_info()
    name=number_list[name]
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
    if "Yes" in send_more:
        get_info()
        writemsg()       


