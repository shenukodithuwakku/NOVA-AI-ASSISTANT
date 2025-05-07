import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import pyttsx3


class NewsTrendsAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')

        
        if len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)  
        else:
            self.engine.setProperty('voice', voices[0].id)  
        
        self.base_url = "https://news.google.com"
        self.keywords = ['technology', 'world']

    def talk(self, text):
        """Speak the given text."""
        print(f"Nova: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def take_command(self):
        """Listen and return voice command as text."""
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for a topic or command...")
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

    def fetch_news(self, keyword):
        """Scrape Google News for a given keyword and return headlines."""
        url = f"{self.base_url}/search?q={keyword}&hl=en-US&gl=US&ceid=US:en"
        try:
            response = requests.get(url)
            response.raise_for_status()  
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = soup.select('article h3 a')
            headlines = []

            for article in articles[:5]:
                title = article.text.strip()
                headlines.append(title)

            return headlines
        except requests.exceptions.RequestException as e:
            return [f"Error fetching news for {keyword}: {e}"]

    def respond_with_news(self, keyword):
        """Speak the top headlines for the given topic."""
        self.talk(f"Fetching top news headlines for {keyword}")
        headlines = self.fetch_news(keyword)

        if not headlines:
            self.talk(f"Sorry, no news found for {keyword}.")
        else:
            for i, headline in enumerate(headlines, 1):
                self.talk(f"Headline {i}: {headline}")

    def run(self):
        """Main loop to run the assistant."""
        self.talk("Hello, I'm your News and Trends assistant. What topic are you interested in?")
        while True:
            command = self.take_command().lower()

            if "stop" in command or "exit" in command or "goodbye" in command:
                self.talk("Goodbye! Stay informed.")
                break

            elif "news about" in command:
                topic = command.replace("news about", "").strip()
                if topic:
                    self.respond_with_news(topic)
                else:
                    self.talk("Please say the topic again.")
            elif command in self.keywords:
                self.respond_with_news(command)
            else:
                self.talk(f"Let me try to fetch news about {command}")
                self.respond_with_news(command)



if __name__ == "__main__":
    assistant = NewsTrendsAssistant()
    assistant.run()
