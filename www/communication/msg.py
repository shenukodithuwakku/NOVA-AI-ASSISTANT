<<<<<<< HEAD
=======
from os import startfile
>>>>>>> a54ae0a38056eab7c433e4f63e8dc48c40076dae
import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
from time import sleep
<<<<<<< HEAD

listener=sr.Recognizer()
engine=pyttsx3.init()
=======
import getpass as gp
import subprocess  
listener = sr.Recognizer()
engine = pyttsx3.init()
>>>>>>> a54ae0a38056eab7c433e4f63e8dc48c40076dae

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
<<<<<<< HEAD
    except:
        talk("Sorry , Did not understand the audio.") 
        pass
=======
    except Exception as e:
        talk("Sorry, did not understand the audio.")
        print(f"Error: {e}")
        return ""
>>>>>>> a54ae0a38056eab7c433e4f63e8dc48c40076dae

def whatsappmsg(number, message, time_hour, time_min):
    kt.sendwhatmsg(number, message, time_hour, time_min)

<<<<<<< HEAD
    kt.sendwhatmsg(name,message,time_hour,time_min)

number_list = {
    "Mom": "+94782511654",
    "dad": "+94771234567",
    "amaya": "+94770000000"
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
=======
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
>>>>>>> a54ae0a38056eab7c433e4f63e8dc48c40076dae
    print(message)
    talk("What hour do you want to send the message?")
    time_hour = get_info()
    try:
        time_hour = int(time_hour)
    except ValueError:
        talk("Invalid hour. Please try again.")
        return

<<<<<<< HEAD
    talk("Whatsapp message has been sent successfully!!")
    talk("Do you want to send more messages")
    send_more=get_info()
    if "yes" in send_more.lower():
        writemsg()

writemsg()
=======
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
>>>>>>> a54ae0a38056eab7c433e4f63e8dc48c40076dae


