from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "FullSearch"

@app.route("/sobre/")
def hello():
    return "Sobre"