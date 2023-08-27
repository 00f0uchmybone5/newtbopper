from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    reutrn "Hello World!\n"