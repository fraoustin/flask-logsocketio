#!/usr/bin/env python
from flask import Flask, render_template, current_app
from flask_socketio import SocketIO, emit
import datetime
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=None)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@app.route('/test')
def test():
    now = datetime.datetime.now()
    emit('my_response',
         {'data': 'coucou', 'time': now.strftime("%d/%m/%Y %H:%M:%S")},
         namespace='/test',
         broadcast=True)
    return 'send msg coucou at %s' % now.strftime("%d/%m/%Y %H:%M:%S")

@socketio.on('my_event', namespace='/test')
def test_reception_msg(message):
    current_app.logger.error("reception message %s" % message)

if __name__ == '__main__':
    socketio.run(app, debug=True)
