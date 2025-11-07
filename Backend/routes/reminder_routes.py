from flask import Blueprint, jsonify, request
import json, os
from services.drug_api_service import get_drug_info

reminder_routes = Blueprint('reminder_routes', __name__)
DATA_FILE = os.path.join('data', 'reminders.json')

# --- Helper functions for saving/loading reminders ---
def load_reminders():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_reminders(reminders):
    with open(DATA_FILE, 'w') as f:
        json.dump(reminders, f, indent=4)

# --- API Routes ---

# Add a new reminder
@reminder_routes.route('/add_reminder', methods=['POST'])
def add_reminder():
    data = request.get_json()
    name = data.get('name')
    dosage = data.get('dosage')
    time = data.get('time')

    if not all([name, dosage, time]):
        return jsonify({"error": "Please provide name, dosage, and time"}), 400

    reminders = load_reminders()
    new_reminder = {"name": name, "dosage": dosage, "time": time}
    reminders.append(new_reminder)
    save_reminders(reminders)

    return jsonify({"message": "Reminder added successfully!", "reminder": new_reminder}), 201


# Get all reminders
@reminder_routes.route('/get_reminders', methods=['GET'])
def get_reminders():
    reminders = load_reminders()
    return jsonify(reminders), 200


# Get drug information
@reminder_routes.route('/drug_info/<drug_name>', methods=['GET'])
def drug_info(drug_name):
    info = get_drug_info(drug_name)
    if "error" in info:
        return jsonify(info), 404
    return jsonify(info), 200
