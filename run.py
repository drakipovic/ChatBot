from live_score.main import socketio, app
import live_score.views

socketio.run(app, host='0.0.0.0', debug=True)