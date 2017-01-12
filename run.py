from chat_bot.main import socketio, app
import chat_bot.views

socketio.run(app, host='0.0.0.0', debug=True)