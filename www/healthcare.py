import datetime
import json
import os
import eel 

eel.init('www')


def set_reminder(reminder, time):
    reminders = load_data("reminders.json")
    reminders.append({"reminder": reminder, "time": time})
    save_data("reminders.json", reminders)
    return f"Reminder set: {reminder} at {time}"

def get_reminders():
    reminders = load_data("reminders.json")
    now = datetime.datetime.now()
    upcoming = []
    for r in reminders:
        reminder_time = datetime.datetime.strptime(r["time"], "%Y-%m-%d %H:%M:%S")
        if reminder_time > now:
            upcoming.append(f"{r['reminder']} at {r['time']}")
    return upcoming


def add_appointment(doctor, date, time):
    appointments = load_data("appointments.json")
    appointments.append({"doctor": doctor, "date": date, "time": time})
    save_data("appointments.json", appointments)
    return f"Appointment added with Dr. {doctor} on {date} at {time}"

def view_appointments():
    appointments = load_data("appointments.json")
    return [f"Appointment with Dr. {a['doctor']} on {a['date']} at {a['time']}" for a in appointments]


def add_schedule(task, date, time):
    schedule = load_data("schedule.json")
    schedule.append({"task": task, "date": date, "time": time})
    save_data("schedule.json", schedule)
    return f"Task added to schedule: {task} on {date} at {time}"

def view_schedule():
    schedule = load_data("schedule.json")
    return [f"Task: {s['task']} on {s['date']} at {s['time']}" for s in schedule]


def track_health_metric(metric, value):
    metrics = load_data("health_metrics.json")
    metrics.append({"metric": metric, "value": value, "date": str(datetime.datetime.now())})
    save_data("health_metrics.json", metrics)
    return f"Health metric recorded: {metric} = {value}"

def view_health_metrics():
    metrics = load_data("health_metrics.json")
    return [f"{m['metric']}: {m['value']} (Recorded on {m['date']})" for m in metrics]

@eel.expose
def chatbot_response(user_input):
    responses = {
        "fever": "It seems like you have a fever. Make sure to stay hydrated and rest. If it persists, consult a doctor.",
        "headache": "For headaches, try to rest in a quiet, dark room and stay hydrated. If it’s severe, consider seeing a doctor.",
        "cough": "A cough could be due to a cold or allergies. Drink warm fluids and monitor your symptoms.",
        "diabetes": "Managing diabetes involves a healthy diet, regular exercise, and monitoring blood sugar levels. Consult your doctor for a personalized plan.",
        "cold": "For a common cold, get plenty of rest, drink fluids, and consider over-the-counter remedies if needed.",
        "sore throat": "A sore throat can be soothed with warm liquids, honey, and rest. If it lasts more than a few days, see a doctor.",
        "stomach ache": "For stomach aches, try to rest and avoid solid food for a few hours. If pain is severe or persistent, consult a doctor.",
        "back pain": "Back pain can often be relieved with rest, gentle stretching, and over-the-counter pain medication.",
        "allergy": "For allergies, avoid known triggers and consider antihistamines. If symptoms are severe, seek medical advice.",
        "asthma": "If you have asthma, use your inhaler as prescribed and avoid triggers. Seek help if you have trouble breathing.",
        "chest pain": "Chest pain can be serious. If you have severe or persistent chest pain, seek emergency medical attention.",
        "high blood pressure": "Monitor your blood pressure regularly, reduce salt intake, exercise, and follow your doctor's advice.",
        "low blood pressure": "Stay hydrated and avoid standing up too quickly. If you feel dizzy or faint, sit or lie down immediately.",
        "vomiting": "If you are vomiting, try to sip clear fluids. If vomiting is severe or lasts more than a day, see a doctor.",
        "diarrhea": "Stay hydrated and avoid dairy or fatty foods. If diarrhea persists for more than 2 days, consult a doctor.",
        "constipation": "Increase fiber intake, drink plenty of water, and exercise regularly. If constipation persists, see a doctor.",
        "insomnia": "For insomnia, try to maintain a regular sleep schedule and avoid screens before bed.",
        "anxiety": "Practice deep breathing, mindfulness, and talk to someone you trust. If anxiety is overwhelming, seek professional help.",
        "depression": "You are not alone. Talk to someone you trust or a mental health professional if you feel persistently sad.",
        "injury": "For minor injuries, clean the wound and apply a bandage. For serious injuries, seek medical attention.",
        "burn": "Cool the burn under running water for 10-20 minutes. Do not apply ice. Seek help for severe burns.",
        "cut": "Clean the cut with water, apply pressure to stop bleeding, and cover with a clean bandage.",
        "sprain": "Rest, ice, compress, and elevate the injured area. If pain or swelling is severe, see a doctor.",
        "fracture": "Immobilize the area and seek medical attention immediately.",
        "hello": "Hi! How can I assist you with your healthcare today?",
        "hi": "Hello! How can I help you with your health concerns?",
        "how are you": "I'm just a program, but I'm here to help you stay healthy!",
        "bye": "Goodbye! Stay healthy!",
        "thank you": "You're welcome! Let me know if you have more questions.",
        "thanks": "Happy to help! Ask me anything about your health."
    }
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    return "I'm sorry, I don't have enough information about that. Please consult a healthcare professional."


def get_diet_recommendation():
    return "Eat a balanced diet with fruits, vegetables, lean proteins, and whole grains."

def get_exercise_recommendation():
    return "Aim for at least 30 minutes of moderate exercise, 5 days a week."


def add_health_record(record):
    records = load_data("health_records.json")
    records.append({"record": record, "date": str(datetime.datetime.now())})
    save_data("health_records.json", records)
    return "Health record added successfully."

def view_health_records():
    records = load_data("health_records.json")
    return [f"Record: {r['record']} (Added on {r['date']})" for r in records]

def load_data(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return json.load(file)

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    eel.start('new.html', size=(900, 700))  # Make sure 'new.html' exists in the www folder
