from app.chatbot import Prompt, is_toxic, chatbot_response
from app.utils import read_datafile

import pytest
from hypothesis import given
from hypothesis.strategies import text
from langchain_community.llms import LlamaCpp
from typing import List


toxic_words_reference = read_datafile('app/toxic_words.txt')
threshold = 0.5


class DummyLlamaCppForTest(LlamaCpp):
    def __init__(self) -> None:
        pass
    
    def invoke(self, prompt: str) -> str:
        return prompt

dummy_llm = DummyLlamaCppForTest()

@pytest.mark.parametrize(
    "prompt_string,expected_result",
    [
        ('12345', 'Question: 12345'),
        ('test_prompt', 'Question: test_prompt'),
        ('Beautiful is better than ugly.', 'Question: Beautiful is better than ugly.'),
        ('Explicit is better than implicit.', 'Question: Explicit is better than implicit.'),
        ('Simple is better than complex.', 'Question: Simple is better than complex.'),
        ('Complex is better than complicated.', 'Question: Complex is better than complicated.'),
        ('Flat is better than nested.', 'Question: Flat is better than nested.'),
        ('Sparse is better than dense.', 'Question: Sparse is better than dense.'),
        ('Readability counts.', 'Question: Readability counts.'),
        ('Special cases aren\'t special enough to break the rules.', 'Question: Special cases aren\'t special enough to break the rules.'),
    ]
)
def test_is_prompt_valid(prompt_string: str, expected_result: str):
    assert Prompt(prompt_string).body == expected_result

@pytest.mark.parametrize(
    "prompt_string,toxic_words_reference,threshold,expected_result",
    [
        (Prompt('12345'), toxic_words_reference, threshold, False),
        (Prompt('test_prompt'), toxic_words_reference, threshold, False),
        (Prompt('Beautiful is better than ugly.'), toxic_words_reference, threshold, False),
        (Prompt('Explicit is better than implicit.'), toxic_words_reference, threshold, False),
        (Prompt('Simple is better than complex.'), toxic_words_reference, threshold, False),
        (Prompt('Complex is better than complicated.'), toxic_words_reference, threshold, False),
        (Prompt('Flat is better than nested.'), toxic_words_reference, threshold, False),
        (Prompt('Sparse is better than dense.'), toxic_words_reference, threshold, False),
        (Prompt('Readability counts.'), toxic_words_reference, threshold, False),
        (Prompt('Special cases aren\'t special enough to break the rules.'), toxic_words_reference, threshold, False),
        (Prompt('fuck fuck fuck.'), toxic_words_reference, threshold, True),
        (Prompt('*itches, 4r5e & 5h1t.'), toxic_words_reference, threshold, True),
    ]
)
def test_is_prompt_toxic(prompt_string: str, toxic_words_reference: List[str], threshold: float, expected_result: bool):
    assert is_toxic(prompt_string, toxic_words_reference, threshold) == expected_result


@pytest.mark.parametrize(
    "prompt_string,llm,expected_result",
    [
        (Prompt('Simple is better than com\nplex.'), dummy_llm, 'Simple is better than com<br>plex.'),
        (Prompt('Complex \nis better than complicated.'), dummy_llm, 'Complex <br>is better than complicated.'),
        (Prompt('Flat is better than nested.'), dummy_llm, 'Flat is better than nested.'),
        (Prompt('Readab\nility counts.'), dummy_llm, 'Readab<br>ility counts.'),
    ]
)
def test_is_chatbot_response_valid(prompt_string: Prompt, llm: LlamaCpp, expected_result: str):
    assert chatbot_response(prompt_string, llm) == expected_result


def encode(input_string):
    if not input_string:
        return []
    count = 1
    prev = ""
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q

@given(text())
def test_decode_inverts_encode(prompt_string: str):
    assert decode(encode(prompt_string)) == prompt_string
