Flask-logsocketio
=================

Flask-logsocketio generate on socketio "log"  log of your application

It use flask-socketio module

Installation
------------

::

    pip install flask-logsocketio
        
Or

::

    git clone https://github.com/fraoustin/flask-logsocketio.git
    cd flask-logsocketio
    python setup.py install

Usage
-----

::
    
    from flask import Flask, request, current_app
    from flask_logsocketio import LogSocketIO

    app = Flask(__name__)
    app.secret_key = 'super secret string'
    app.register_blueprint(LogSocketIo(ui_testing=True))

    @app.route("/")
    def hello():
        current_app.logger.error("error from hello")
        current_app.logger.info("info from hello")
        current_app.logger.debug("debug from hello")
        return "Hello World!"

    if __name__ == "__main__":
        app.run(port=8080)
