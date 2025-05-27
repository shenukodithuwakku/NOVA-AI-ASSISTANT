from os import startfile
import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
from time import sleep
import getpass as gp
import subprocess  
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('\nListening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except Exception as e:
        talk("Sorry, did not understand the audio.")
        print(f"Error: {e}")
        return ""

def whatsappmsg(number, message, time_hour, time_min):
    kt.sendwhatmsg(number, message, time_hour, time_min)

number_list = {"amma": "+94782511654"}  # Use lowercase keys and international format

def writemsg():
    talk("To whom do you want to send WhatsApp message?")
    print("To whom do you want to send WhatsApp message?")
    name = get_info().strip().lower()
    number = number_list.get(name)
    if not number:
        talk("Sorry, I don't have the number for that contact.")
        print("Contact not found.")
        return

    print(number)
    talk("What is the message you want to send?")
    print("What is the message you want to send?")
    message = get_info()
    print(message)
    talk("What hour do you want to send the message?")
    time_hour = get_info()
    try:
        time_hour = int(time_hour)
    except ValueError:
        talk("Invalid hour. Please try again.")
        return

    talk("What minute do you want to send the message?")
    time_min = get_info()
    try:
        time_min = int(time_min)
    except ValueError:
        talk("Invalid minute. Please try again.")
        return

    print(f"{time_hour}:{time_min}")
    whatsappmsg(number, message, time_hour, time_min)
    print("WhatsApp message has been sent successfully!!")
    talk("WhatsApp message has been sent successfully!!")
    talk("Do you want to send more messages?")
    send_more = get_info()
    if "yes" in send_more.lower():
        writemsg()

# New function to run external Python script
def run_external_script():
    try:
        subprocess.Popen(["python", r"c:\Users\Lenovo\Documents\GitHub\NOVA-AI-ASSISTANT\www\communication\msg.py"])
        talk("External script has been started.")
    except Exception as e:
        talk("Failed to start external script.")
        print(f"Error: {e}")

# Install required packages
subprocess.check_call(["C:/Program Files/Python314/python.exe", "-m", "pip", "install", "SpeechRecognition", "pyttsx3", "pywhatkit"])


