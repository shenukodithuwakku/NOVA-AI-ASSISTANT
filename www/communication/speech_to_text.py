import speech_recognition as sr
import pyttsx3
import pywhatkit as kit

r = sr.Recognizer()

def record_text():

    while(1):
        try:

            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.Listen(source2)

                MyText = r.recognize_google(audio2)


        except sr.RequestError as e:
<<<<<<< HEAD
            print("Could not request results; {0}".format(e))
=======
           print("Could not request results; {0}".format(e))
>>>>>>> a54ae0a38056eab7c433e4f63e8dc48c40076dae

        except sr.UnknownValueError:
            print("unknown error occurred")

        return

def output_text(text):
    f = open("output.text", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = record_text()
    output_text(text)

    print("Wrote text")