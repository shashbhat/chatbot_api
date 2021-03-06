from chatbot import chatbot
from flask import Flask, render_template, request
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)
# app.static_folder = 'static'

@app.route("/")
def home():
    return "Hello"

@app.route('/check')
def message():
    return {"message":"Check you luck"}

@app.route("/chat/<msg>")
def get_bot_response(msg):

    return str(chatbot.get_response(msg))
 
if __name__ == "__main__":
    app.run() 