from flask import Flask, send_file
from flask_socketio import SocketIO
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket = SocketIO(app)

PUBLIC_FOLDER = os.path.join(os.getcwd(), 'public')
BUILD_FOLDER = os.path.join(PUBLIC_FOLDER, 'build')

@app.route('/', methods=["GET"])
def index():
    return send_file(os.path.join(PUBLIC_FOLDER, 'index.html'))

@app.route('/<fileName>', methods=["GET"])
def public_file_get(fileName):
    return send_file(os.path.join(PUBLIC_FOLDER, fileName))

@app.route('/build/<fileName>', methods=["GET"])
def public_build_file_get(fileName):
    return send_file(os.path.join(BUILD_FOLDER, fileName))

@socket.on('user connected')
def userConnected(id):
    print("USER {} CONNECTED!".format(id))

if __name__ == "__main__":
    socket.run(app)