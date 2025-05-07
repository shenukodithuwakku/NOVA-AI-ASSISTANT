import speech_recognition as sr
import wikipedia
import datetime
import pyttsx3


class GeneralQuestionAnswering:
    def __init__(self):
        wikipedia.set_lang("en")
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)  

    def talk(self, command):
        """Speak the given command using text-to-speech."""
        print(f"Nova: {command}")
        self.engine.say(command)
        self.engine.runAndWait()

    def take_command(self):
        """Listen for a voice command and return it as text."""
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Sorry, there was a network error."

    def answer(self, user_input):
        """Process user input and return a response."""
        user_input_lower = user_input.lower()

        if "time" in user_input_lower:
            return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."

        elif "date" in user_input_lower:
            return f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}."

        elif "your name" in user_input_lower:
            return "I'm Nova!"

        elif "who are you" in user_input_lower:
            return "I'm Nova, your personal AI assistant."

        elif "how can you help" in user_input_lower:
            return "I can answer your questions, provide information, and assist you with tasks."

        elif "stop" in user_input_lower or "exit" in user_input_lower:
            return "Goodbye!"

        else:
            try:
                summary = wikipedia.summary(user_input, sentences=2)
                return summary
            except wikipedia.exceptions.DisambiguationError as e:
                return f"Your question is too broad. Try being more specific. Suggestions: {e.options[:3]}"
            except wikipedia.exceptions.PageError:
                return "Sorry, I couldn't find any information on that topic."
            except Exception as e:
                return f"Oops! Something went wrong: {str(e)}"



if __name__ == "__main__":
    assistant = GeneralQuestionAnswering()
    while True:
        command = assistant.take_command()
        if not command.strip():
            continue
        response = assistant.answer(command)
        assistant.talk(response)
        if "goodbye" in response.lower():
            break
