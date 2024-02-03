from typing import Dict, List, Any
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp
    

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])


def load_llm() -> LlamaCpp:
    return LlamaCpp(
        model_path="../phi-2.Q4_K_M.gguf",
        temperature=0.75,
        max_tokens=2000,
        top_p=1,
        callback_manager=callback_manager,
        verbose=True,  # Verbose is required to pass to the callback manager
)


class Prompt(str):
    def __init__(self, body: str) -> None:
        self.body = f'Question: {body}'
 

def chatbot_response(prompt: Prompt, llm: LlamaCpp) -> str:
    response = llm.invoke(prompt).replace('\n', '<br>').replace('    ', '&nbsp;'*4)
    return response


def is_toxic(prompt: Prompt, toxic_words_reference: Any, threshold: float) -> bool:
    toxic_words_reference = [str(x) for x in toxic_words_reference]
    toxicity = 0.0
    words = prompt.body
    words = words.replace(',', '').replace('.', '')
    for word in words.split(' '):
        word = word.lower()
        if word in toxic_words_reference:
            toxicity += 1 / len(words.split(' '))
            if toxicity >= threshold:
                return True
    return False
