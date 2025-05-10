import datetime
import json
import os

# Reminders
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

# Appointments
def add_appointment(doctor, date, time):
    appointments = load_data("appointments.json")
    appointments.append({"doctor": doctor, "date": date, "time": time})
    save_data("appointments.json", appointments)
    print(f"Appointment added with Dr. {doctor} on {date} at {time}")

def view_appointments():
    appointments = load_data("appointments.json")
    for a in appointments:
        print(f"Appointment with Dr. {a['doctor']} on {a['date']} at {a['time']}")

# Schedule
def add_schedule(task, date, time):
    schedule = load_data("schedule.json")
    schedule.append({"task": task, "date": date, "time": time})
    save_data("schedule.json", schedule)
    print(f"Task added to schedule: {task} on {date} at {time}")

def view_schedule():
    schedule = load_data("schedule.json")
    for s in schedule:
        print(f"Task: {s['task']} on {s['date']} at {s['time']}")

# Health Metrics Tracking
def track_health_metric(metric, value):
    metrics = load_data("health_metrics.json")
    metrics.append({"metric": metric, "value": value, "date": str(datetime.datetime.now())})
    save_data("health_metrics.json", metrics)
    print(f"Health metric recorded: {metric} = {value}")

def view_health_metrics():
    metrics = load_data("health_metrics.json")
    for m in metrics:
        print(f"{m['metric']}: {m['value']} (Recorded on {m['date']})")

# Chatbot
def chatbot_response(user_input):
    responses = {
        "hello": "Hi! How can I assist you with your healthcare today?",
        "how are you": "I'm just a program, but I'm here to help you stay healthy!",
        "bye": "Goodbye! Stay healthy!"
    }
    return responses.get(user_input.lower(), "I'm sorry, I didn't understand that.")

# Diet and Exercise Recommendations
def get_diet_recommendation():
    return "Eat a balanced diet with fruits, vegetables, lean proteins, and whole grains."

def get_exercise_recommendation():
    return "Aim for at least 30 minutes of moderate exercise, 5 days a week."

# Health Records Storage
def add_health_record(record):
    records = load_data("health_records.json")
    records.append({"record": record, "date": str(datetime.datetime.now())})
    save_data("health_records.json", records)
    print("Health record added successfully.")

def view_health_records():
    records = load_data("health_records.json")
    for r in records:
        print(f"Record: {r['record']} (Added on {r['date']})")

# Utility Functions for Data Storage
def load_data(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return json.load(file)

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Example Usage
if __name__ == "__main__":
    # Set a reminder
    set_reminder("Take medication", "2025-05-10 18:00:00")
    get_reminders()

    # Add an appointment
    add_appointment("Smith", "2025-05-12", "10:00 AM")
    view_appointments()

    # Add a task to the schedule
    add_schedule("Morning Walk", "2025-05-11", "07:00 AM")
    view_schedule()

    # Track health metrics
    track_health_metric("Blood Pressure", "120/80")
    view_health_metrics()

    # Chatbot interaction
    print(chatbot_response("hello"))

    # Diet and exercise recommendations
    print(get_diet_recommendation())
    print(get_exercise_recommendation())

    # Add and view health records
    add_health_record("Routine check-up: All good.")
    view_health_records()