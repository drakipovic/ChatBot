from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask('LiveScore', template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)