from flask import render_template, request, session, jsonify
from flask_socketio import emit
from main import app, socketio


answers = {
    'hello': 'Hello, how are you?',
    'how are you?': "I'm fine thanks for asking, how are you?",
    'did barca win today?': 'Yes they did, 3:1.',
    "what's your name?": "I can't say that, I'm shy",
    "bok": "I' can't understand that, did you mean book? What book?",
    "kako si": "What is kako? Is this spanish? Yes?"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    username = request.form.get('username')
    return jsonify({'username': username})

@socketio.on('question')
def send_response(question):
    answer = answers.get(question['data'].lower(), "I'm sorry, I'dont understand this.")
    emit('response', {'data': answer})