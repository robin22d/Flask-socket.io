#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from random import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

Disk = "Everything"

@app.route('/')
def index():
    return render_template('index.html', disk=Disk)


dict = {'Disk0': 0, 'Disk1': 0,  'Disk2': 0}

@socketio.on('get_data')
def join(message):
    dict['Disk0'] = randint(1, 100)
    dict['Disk1'] = randint(1, 100)
    dict['Disk2'] = randint(1, 100)
    emit('post_data', dict)
    emit('post_graph_data', dict)



if __name__ == '__main__':
    socketio.run(app, debug=True)
