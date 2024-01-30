
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp
from flask import Flask, jsonify, render_template, request


#install gunicorn


# callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
# llm = LlamaCpp(
#     model_path="phi-2.Q4_K_M.gguf",
#     temperature=0.75,
#     max_tokens=2000,
#     top_p=1,
#     callback_manager=callback_manager,
#     verbose=True,  # Verbose is required to pass to the callback manager
# )


def chatbot_response(msg: str) -> str:
    prompt = f'Question: {msg}'
    return 'hui'
    # return llm.invoke(msg)

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userPrompt = request.args.get('msg')
    return chatbot_response(userPrompt)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
