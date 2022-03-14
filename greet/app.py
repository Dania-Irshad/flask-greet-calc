from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    """Return "welcome"."""
    html = "<html><body><h1>welcome</h1></body></html>"
    return html

@app.route('/welcome/home')
def home():
    """Return "welcome home"."""
    html = "<html><body><h1>welcome home</h1></body></html>"
    return html

@app.route('/welcome/back')
def welcome_back():
    """Return "welcome back"."""
    html = "<html><body><h1>welcome back</h1></body></html>"
    return html