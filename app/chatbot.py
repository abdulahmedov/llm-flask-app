from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp


# callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
# llm = LlamaCpp(
#     model_path="/llm-flask-app/phi-2.Q4_K_M.gguf",
#     temperature=0.75,
#     max_tokens=2000,
#     top_p=1,
#     callback_manager=callback_manager,
#     verbose=True,  # Verbose is required to pass to the callback manager
# )

# def chatbot_response(msg: str, llm: LlamaCpp=llm) -> str:
#     prompt = f'Question: {msg}'
#     return llm.invoke(msg)

def chatbot_response(msg: str,) -> str:
    return msg
