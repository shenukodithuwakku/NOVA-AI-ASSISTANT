import pyttsx3
import speech_recognition as sr
from datetime import datetime

def speak(message):
    """Speak the given message."""
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def listen_for_command():
    """Listen for a voice command and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            return "I didn't understand that."
        except sr.RequestError:
            return "There was an issue with the speech recognition service."
        

def main():
    """Main function to listen for a command and respond with the current time."""
    command = listen_for_command()

    if "what is the time now" in command:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")  
        speak(f"The current time is {current_time}.")
    else:
        speak("I can only tell you the time if you ask 'what is the time now'.")

    if "what is the time now"in command or "tell the time" in command or "Nova please tell the time" in command or "Time please" in command or "Nova what is the time" in command :
        now = datetime.now()
        current_time = now.strftime("%I:%M %p") 
        speak(f"The time is.... {current_time}.")
    elif command == "":
        speak("Sorry, I didn't catch that. Please try again.")    
    else:
        speak("Sorry, I didn't clear that.. Please try again." in command or "I can't understand..please tell again")


if __name__ == "__main__":
    main()