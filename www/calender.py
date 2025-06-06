<<<<<<< HEAD
import datetime

# Dictionary to store events
calendar = {}

def add_event(date, event):
    """Add an event to the calendar."""
    if date in calendar:
        calendar[date].append(event)
    else:
        calendar[date] = [event]
    print(f"Event '{event}' added on {date}.")

def view_events(date):
    """View events for a specific date."""
    if date in calendar:
        print(f"Events on {date}:")
        for i, event in enumerate(calendar[date], start=1):
            print(f"{i}. {event}")
    else:
        print(f"No events found on {date}.")

def delete_event(date, event_index):
    """Delete an event from the calendar."""
    if date in calendar and 0 < event_index <= len(calendar[date]):
        removed_event = calendar[date].pop(event_index - 1)
        print(f"Event '{removed_event}' removed from {date}.")
        if not calendar[date]:  # Remove the date if no events remain
            del calendar[date]
    else:
        print("Invalid date or event index.")

def main():
    """Main function to manage the calendar."""
    while True:
        print("\nCalendar Menu:")
        print("1. Add Event")
        print("2. View Events")
        print("3. Delete Event")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")  # Validate date format
                event = input("Enter the event description: ")
                add_event(date, event)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")  # Validate date format
                view_events(date)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")  # Validate date format
                view_events(date)
                if date in calendar:
                    event_index = int(input("Enter the event number to delete: "))
                    delete_event(date, event_index)
            except ValueError:
                print("Invalid input. Please use the correct format.")
        elif choice == "4":
            print("Exiting the calendar. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
=======
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

    if "what is today" in command:
        today = datetime.now().strftime("%A, %d %B %Y")  
        speak(f"Today is.. {today}.")

    if "what day is it today" in command:
        today = datetime.now().strftime("%A, %d %B %Y")  # Format: Day, DD Month YYYY
        speak(f"Today is {today}.")
<<<<<<< HEAD

    else:  
         speak("Sorry, I didn't understand that command.")
=======
<<<<<<< Updated upstream
    
=======
>>>>>>> Stashed changes
    else:
        speak("Sorry, I didn't understand that command.")
>>>>>>> 9f019b019fec7901c3e33a10c78ce7e37289aecb
>>>>>>> a54ae0a38056eab7c433e4f63e8dc48c40076dae

if __name__ == "__main__":
    main()