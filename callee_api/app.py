from flask import Flask
from requests import get

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "From Cloud Run"

@app.route("/check_web")
def check_web():
    result = get("https://www.google.com")
    return f"Status of caller : {result.text}"
