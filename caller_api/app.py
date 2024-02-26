import os

from flask import Flask
from requests import get

app = Flask(__name__)

SERVICE_URL = os.getenv("SERVICE_URL")


@app.route("/")
def hello_world():
    result = get(SERVICE_URL)
    return f"<h1>Hello, {result.text}!</h1>"

@app.route("/check_web")
def check_web():
    result = get("https://www.google.com")
    return f"Status of caller : {result.text}"

@app.route("/check_web_callee")
def check_web2():
    result = get(f"{SERVICE_URL}/check_web")
    return f"Status of callee : {result.text}"
