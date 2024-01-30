from chatbot import chatbot_response, llm
from chatbot import chatbot_response

from flask import Flask, render_template, request


app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/post", methods=['POST'])
def get_bot_response():
    userPrompt = request.form['msg']
    return chatbot_response(userPrompt, llm)
