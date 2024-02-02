from typing import Dict, List
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp


class DummyLlamaCppForTest(LlamaCpp):
    def __init__(self) -> None:
        pass
    
    def invoke(self, prompt: str) -> str:
        return prompt
    

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
 

# class Intent(str):
#     def __init__(self, prompt: Prompt) -> None:
#         pass


# class IntentClassfier:
#     def __init__(self) -> None:
#         pass

#     def classify(self, intent: Prompt) -> Skill:
#         return Skill
    
#     def calculate_levenstein(self, string):




# class PromptEngineer:
#     def __init__(self) -> None:
#         pass

#     def classify_intent() -> None:
#         pass
    
#     def build_prompt(self, intent: Intent) -> Prompt:
#         return


# class Skill:
#     def __init__(self, name: str, question: str) -> None:
#         self.name = name
#         self.question = question
    
#     def ask_query(self):
#         return Response(self.question)
    
#     def process_query(self, query: str, llm: LlamaCpp) -> Response:
#         pass 
    
#     def exit(self, arg):
#         pass

#     def __repr__(self):
#         pass

#     def __str__(self):
#         pass


# class SkillSelector:
#     def __init__(self, model, skills: List[Skill], classify_method: str) -> None:
#         self.model = model
#         self.skills = skills

#     def select_skill(self, intent: Prompt):
#         return self.skills



# from dataclasses import dataclass


# @dataclass
# class State:
#     val: str = 'init'


# class DialogueFlow:
#     def __init__(self, current: State) -> None:
#         self.current = current
#         self.previous = None


# class ChatBot:
#     def __init__(self, skill_selector: SkillSelector) -> None:
#         self.skill_selector = skill_selector
#         self.state = State()
#         self.dialogue_flow = DialogueFlow(self.state)
    
#     def run():
#         if self.state == 'init':
#             return Response('Hi, I am AI powered bot')
        
#         elif self.state
    
#     def process_intent(self, intent: Intent):
#         self.state, self.skill = self.skill_selector(intent)
#         self.skills[self.state].ask

#     def response(self, Prompt):
#         if self.state == 'init':
#             pass
#         elif self.state == 'skill':
#             pass

#     def move_back(self) -> None:
#         self.dialogue_flow.current = self.dialogue_flow.previous
    
#     def move_forward(self, skill: Skill) -> None:
#         self.dialogue_flow.previous = self.dialogue_flow.current
#         self.dialogue_flow.current = skill.name

    
#     def step_back(self):
#         pass

#     def reset(self):
#         pass

#     def joke(self):
#         pass


def chatbot_response(prompt: Prompt, llm: LlamaCpp) -> str:
    response = llm.invoke(prompt).replace('\n', '<br>').replace('    ', '&nbsp;'*4)
    return response


def is_toxic(prompt: Prompt, toxic_words_reference: List[str], threshold: float) -> bool:
    toxicity = 0
    words = prompt.body
    words = words.replace(',', '').replace('.', '')
    words = words.split(' ')
    for word in words:
        word = word
        if word in toxic_words_reference:
            toxicity += 1 / len(words)
            if toxicity >= threshold:
                return True
    return False
