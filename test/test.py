from flask import Flask, request, current_app
from flask_logsocketio import LogSocketIo

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
