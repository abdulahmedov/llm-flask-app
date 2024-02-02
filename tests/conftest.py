from app.chatbot import Prompt, is_toxic

from typing import Callable, TypeVar, Generic
import pytest


T = TypeVar('T')

class Fixture(Generic[T]):
    pass

@pytest.fixture
def toxic_prompt() -> Prompt:
    return Prompt()

@pytest.fixture
def non_toxic_prompt() -> Prompt:
    return Prompt()

@pytest.fixture
def fabric_prompt() -> Callable:
    def non_toxic_prompt() -> Prompt:
        return Prompt()
    return non_toxic_prompt()


def test_toxic_prompt(toxic_prompt: Fixture[Prompt]):
    assert isinstance(toxic_prompt, str)
    assert is_toxic(toxic_prompt) is True


def test_non_toxic_prompt(non_toxic_prompt: Fixture[Prompt]):
    assert isinstance(non_toxic_prompt, str)
    assert is_toxic(non_toxic_prompt) is False


def test_fixture_fabric(fabric_prompt: Callable):
    assert fabric_prompt() is Prompt
    assert is_toxic(fabric_prompt()) is False
