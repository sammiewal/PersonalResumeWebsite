from datetime import date
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/education")
def index():
    return render_template("education.html")
    
@app.route("/work")
def about_me():
    return render_template("work.html")
    
@app.route("/home")    
def home():
    return render_template("home.html")