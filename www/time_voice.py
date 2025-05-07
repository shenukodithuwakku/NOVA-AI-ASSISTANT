import pyttsx3
from datetime import datetime

def speak_time():
    """Speak the current time."""
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Get the current time
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")  # Format: HH:MM AM/PM

    # Prepare the message
    message = f"The current time is {current_time}."

    # Speak the message
    engine.say(message)
    engine.runAndWait()

if __name__ == "__main__":
    speak_time()