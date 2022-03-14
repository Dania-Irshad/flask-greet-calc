from crypt import methods
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def add_numbers():
    """Add a and b and return sum."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    html = f"<html><body><h1>{add(a, b)}</h1></body></html>"
    return html

@app.route('/sub')
def subtract_numbers():
    """Subtract b from a and return difference."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    html = f"<html><body><h1>{sub(a, b)}</h1></body></html>"
    return html

@app.route('/mult')
def multiply_numbers():
    """Multiply a and b and return product."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    html = f"<html><body><h1>{mult(a, b)}</h1></body></html>"
    return html

@app.route('/div')
def divide_numbers():
    """Divide a by b and return quotient."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    html = f"<html><body><h1>{div(a, b)}</h1></body></html>"
    return html

@app.route('/math/<operation>')
def all_operations(operation):
    """Run the operation requested and return result."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    REQS = {
        "add": add(a, b),
        "sub": sub(a, b),
        "mult": mult(a, b),
        "div": div(a, b)
    }
    result = REQS.get(operation)
    return f"<html><body><h1>{result}</h1></body></html>"
