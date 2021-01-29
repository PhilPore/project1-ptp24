import os 
import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def init_main():
    print("Kernel")
    return render_template("index.html") #will have to pass data in here.

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )