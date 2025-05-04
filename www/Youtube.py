import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser

def talk(command):
    """Speak the given command using text-to-speech."""
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    engine.say(command)
    engine.runAndWait()

def takeCommand():
    """Listen for a voice command and execute the corresponding action."""
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source) 
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()  
            print(f"Command received: {command}")

            if 'play' in command:
                song = command.replace('play', '').strip()
                talk(f"Playing {song} on YouTube")
                pywhatkit.playonyt(song)
            elif 'open youtube' in command:
                talk("Hey dear.....Please wait.....Your request is processing now......Opening youtube now....")
                webbrowser.open("https://www.youtube.com")
            elif 'open facebook' in command:
                talk("Hey dear.....Please wait.....Your request is processing now......Opening Facebook now....")
                webbrowser.open("https://www.facebook.com")
            elif 'open whatsapp' in command:
                talk("Hey dear.....Please wait.....Your request is processing now......Opening WhatsApp now....")
                webbrowser.open("https://web.whatsapp.com")
            elif 'open google' in command:
                talk("Hey dear.....Please wait.....Your request is processing now......Opening Google now....")
                webbrowser.open("https://www.google.com")
            elif 'open email' in command:
                talk("Hey dear.....Please wait.....Your request is processing now......Opening Email now....")
                webbrowser.open("https://mail.google.com")
            elif 'open github' in command:
                talk("Hey dear.....Please wait.....Your request is processing now......Opening Github now....")
                webbrowser.open("https://www.github.com")
            elif 'open microsoft word' in command:
                talk("Hey dear.....Please wait.....Your request is processing now......Opening Microsoft Word now....")
                webbrowser.open("https://www.office.com/launch/word")
            elif 'open microsoft powerpoint' in command:
                talk("Hey dear.....Please wait.....Your request is processing now......Opening Powerpoint now....")
                webbrowser.open("https://www.office.com/launch/powerpoint")
            elif 'open microsoft excel' in command:
                talk("Hey dear.....Please wait.....Your request is processing now......Opening Excel now....")
                webbrowser.open("https://www.office.com/launch/excel")
            elif 'open viber' in command:
                talk("Hey dear.....Please wait.....Your request is processing now......Opening Viber now....")
                webbrowser.open("https://www.viber.com/en/download/")
            elif 'open imo' in command:
                talk("Hey dear.....Please wait.....Your request is processing now......Opening imo now....")
                webbrowser.open("https://www.imo.com/en/download/")                    
            else:
                talk("Sorry dear, I didn't understand that command.")
                print("No valid command detected.")
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio.")
        talk("Sorry, I did not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        talk("There was an issue with the speech recognition service.")
    except Exception as e:
        print(f"Error: {e}")
        talk("An error occurred while processing your command.")

if __name__ == "__main__":
    takeCommand()