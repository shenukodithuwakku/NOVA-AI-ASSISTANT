from flask import Flask, request, jsonify, render_template
from healthcare import (
    set_reminder, get_reminders, add_appointment, view_appointments,
    add_schedule, view_schedule, track_health_metric, view_health_metrics,
    chatbot_response, get_diet_recommendation, get_exercise_recommendation,
    add_health_record, view_health_records
)

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')  # Create an index.html file in a 'templates' folder

# Reminders
@app.route('/set_reminder', methods=['POST'])
def set_reminder_route():
    data = request.json
    set_reminder(data['reminder'], data['time'])
    return jsonify({"message": "Reminder set successfully!"})

@app.route('/get_reminders', methods=['GET'])
def get_reminders_route():
    reminders = get_reminders()
    return jsonify(reminders)

# Appointments
@app.route('/add_appointment', methods=['POST'])
def add_appointment_route():
    data = request.json
    add_appointment(data['doctor'], data['date'], data['time'])
    return jsonify({"message": "Appointment added successfully!"})

@app.route('/view_appointments', methods=['GET'])
def view_appointments_route():
    appointments = view_appointments()
    return jsonify(appointments)

# Chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot_route():
    user_input = request.json['message']
    response = chatbot_response(user_input)
    return jsonify({"response": response})

# Diet and Exercise
@app.route('/diet', methods=['GET'])
def diet_route():
    return jsonify({"recommendation": get_diet_recommendation()})

@app.route('/exercise', methods=['GET'])
def exercise_route():
    return jsonify({"recommendation": get_exercise_recommendation()})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)