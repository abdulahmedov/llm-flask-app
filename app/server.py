from chatbot import chatbot_response, load_llm, is_toxic, Prompt
from utils import read_datafile

from flask import Flask, render_template, request


llm = load_llm()
toxic_words_reference = read_datafile('toxic_words.txt')
threshold = 0.5

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home() -> str:
    return render_template("index.html")

@app.route("/post", methods=['POST'])
def get_bot_response() -> str:
    userPrompt = Prompt(request.form['msg'])
    if is_toxic(userPrompt, toxic_words_reference, threshold):
        response = 'Your prompt is toxic'
    else:
        response = chatbot_response(userPrompt, llm)
    return response
