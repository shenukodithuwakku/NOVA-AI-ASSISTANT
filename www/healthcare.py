import datetime
import json
import os
import speech_recognition as sr

def set_reminder(reminder, time):
    reminders = load_data("reminders.json")
    reminders.append({"reminder": reminder, "time": time})
    save_data("reminders.json", reminders)
    print(f"Reminder set: {reminder} at {time}")

def get_reminders():
    reminders = load_data("reminders.json")
    now = datetime.datetime.now()
    for r in reminders:
        reminder_time = datetime.datetime.strptime(r["time"], "%Y-%m-%d %H:%M:%S")
        if reminder_time > now:
            print(f"Upcoming Reminder: {r['reminder']} at {r['time']}")

def add_appointment(doctor, date, time):
    appointments = load_data("appointments.json")
    appointments.append({"doctor": doctor, "date": date, "time": time})
    save_data("appointments.json", appointments)
    print(f"Appointment added with Dr. {doctor} on {date} at {time}")

def view_appointments():
    appointments = load_data("appointments.json")
    for a in appointments:
        print(f"Appointment with Dr. {a['doctor']} on {a['date']} at {a['time']}")


def add_schedule(task, date, time):
    schedule = load_data("schedule.json")
    schedule.append({"task": task, "date": date, "time": time})
    save_data("schedule.json", schedule)
    print(f"Task added to schedule: {task} on {date} at {time}")

def view_schedule():
    schedule = load_data("schedule.json")
    for s in schedule:
        print(f"Task: {s['task']} on {s['date']} at {s['time']}")


def track_health_metric(metric, value):
    metrics = load_data("health_metrics.json")
    metrics.append({"metric": metric, "value": value, "date": str(datetime.datetime.now())})
    save_data("health_metrics.json", metrics)
    print(f"Health metric recorded: {metric} = {value}")

def view_health_metrics():
    metrics = load_data("health_metrics.json")
    for m in metrics:
        print(f"{m['metric']}: {m['value']} (Recorded on {m['date']})")


def chatbot_response(user_input):
    responses = {
        "fever": "It seems like you have a fever. Make sure to stay hydrated and rest. If it persists, consult a doctor.",
        "headache": "For headaches, try to rest in a quiet, dark room and stay hydrated. If it’s severe, consider seeing a doctor.",
        "cough": "A cough could be due to a cold or allergies. Drink warm fluids and monitor your symptoms.",
        "diabetes": "Managing diabetes involves a healthy diet, regular exercise, and monitoring blood sugar levels. Consult your doctor for a personalized plan.",
        "hello": "Hi! How can I assist you with your healthcare today?",
        "how are you": "I'm just a program, but I'm here to help you stay healthy!",
        "bye": "Goodbye! Stay healthy!"
    }
    return responses.get(user_input.lower(), "I'm sorry, I don't have enough information about that. Please consult a healthcare professional.")


def get_diet_recommendation():
    return "Eat a balanced diet with fruits, vegetables, lean proteins, and whole grains."

def get_exercise_recommendation():
    return "Aim for at least 30 minutes of moderate exercise, 5 days a week."


def add_health_record(record):
    records = load_data("health_records.json")
    records.append({"record": record, "date": str(datetime.datetime.now())})
    save_data("health_records.json", records)
    print("Health record added successfully.")

def view_health_records():
    records = load_data("health_records.json")
    for r in records:
        print(f"Record: {r['record']} (Added on {r['date']})")


def load_data(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return json.load(file)

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your health problem...")
        try:
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")
            return user_input
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None


if __name__ == "__main__":
    print("Welcome to the Healthcare Assistant!")
    print("You can speak your health problem, and I will try to assist you.")
    
    while True:
        user_input = speech_to_text()
        if user_input:
            if "exit" in user_input.lower() or "bye" in user_input.lower():
                print("Goodbye! Stay healthy!")
                break
            else:
                response = chatbot_response(user_input)
                print(f"Assistant: {response}")