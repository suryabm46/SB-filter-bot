from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "SB_KANNADA_MOVE_WORLD"

