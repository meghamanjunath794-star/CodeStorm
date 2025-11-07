from flask import Flask
from routes.reminder_routes import reminder_routes  # ✅ Add this line

app = Flask(__name__)

# Register the reminder routes blueprint
app.register_blueprint(reminder_routes)

@app.route('/')
def home():
    return {
        "message": "Welcome to the Medication Reminder API!",
        "routes": {
            "/add_reminder": "POST - Add a reminder",
            "/get_reminders": "GET - View all reminders",
            "/drug_info/<drug_name>": "GET - Get info about a drug"
        }
    }

if __name__ == '__main__':
    app.run(debug=True)
