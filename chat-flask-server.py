from flask import Flask
from flask_socketio import SocketIO

app = Flask(_name_)
socketio = SocketIO(app)

@app.route('/')
def messageReceived(methods=['GET', 'POST']):
    print('Mensagem recebida!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug = True)