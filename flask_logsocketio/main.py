#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join, dirname
from logging import Handler, NOTSET
import datetime
import time

from flask import Flask, app, current_app,request, Blueprint, send_from_directory
from flask_socketio import SocketIO, emit


def static_web_index():
    return send_from_directory(join(dirname(__file__),'ui'),"index.html")

def static_web(filename):
    if filename == "index.html":
        return redirect(request.url[:-1 * len('index.html')])
    return send_from_directory(join(dirname(__file__),'ui'),filename)

class SocketIoHandler(Handler):

    def __init__(self, level=NOTSET):
        Handler.__init__(self, level)

    def emit(self, record):
         now = datetime.datetime.now()
         emit('logging',
            {
                'msg': self.format(record),
                'time': now.strftime("%d/%m/%Y %H:%M:%S")
            },
            namespace='/log',
            broadcast=True)

class LogSocketIo(Blueprint):

    def __init__(self, name='logsocketio', import_name=__name__, ui_testing=False, level=NOTSET, *args, **kwargs):
        Blueprint.__init__(self, name, import_name, *args, **kwargs)
        self._level = level
        if ui_testing:
            self.add_url_rule('/ui/<path:filename>', 'static_web', static_web)
            self.add_url_rule('/ui/', 'static_web_index', static_web_index)
   
    def register(self, app, options, first_registration=False):
        Blueprint.register(self, app, options, first_registration)
        self._socketio = SocketIO(app, async_mode=None)
        app.logger.addHandler(SocketIoHandler(self._level))
        app.run = self.hack_run
        self._app = app
    
    def hack_run(self, host=None, port=None, debug=None, **options):
        options['threaded'] = True
        Flask.run(self._app, host, port, debug, **options)    


