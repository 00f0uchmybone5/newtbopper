from telnetlib import theNULL
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!\n"
if (i < 0):
    theNULL