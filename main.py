from flask import Flask, request, jsonify, render_template, session
import json
import os
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

def append_to_json(file_name, data):
    try:
        with open(file_name, "r") as json_file:
            existing_data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = {}

    username = data['username']
    if username in existing_data:
        print(f"Overwriting data for user {username}")
    existing_data[username] = data

    with open(file_name, "w") as json_file:
        json.dump(existing_data, json_file, indent=4)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/location', methods=['POST'])
def update_location():
    user_data = request.get_json()
    if 'username' not in session:
        session['username'] = str(uuid.uuid4().hex)  # Use a random session ID
    user_data['username'] = session['username']
    append_to_json("data.json", user_data)
    return jsonify({'status': 'success'}), 200



if __name__ == '__main__':
    app.run(debug=True)
