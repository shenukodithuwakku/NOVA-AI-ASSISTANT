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
    """Main function to listen for a command and respond with the current date."""
    command = listen_for_command()
    if "what day is it today" in command:
        today = datetime.now().strftime("%A, %d %B %Y")  # Format: Day, DD Month YYYY
        speak(f"Today is {today}.")
<<<<<<< Updated upstream
    
=======
>>>>>>> Stashed changes
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()