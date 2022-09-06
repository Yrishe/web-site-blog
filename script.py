#This file has the backend script 

from flask import Flask, render_template, request 
from wtforms import StringField, SubmitField 
from flask_wtf import FlaskForm 

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECrET_pRoJET" 

@app.route('/', ["GET", "POST"])
def index():
  pass 

