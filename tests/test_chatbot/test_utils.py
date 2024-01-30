from app.chatbot import chatbot_response 


response = 'aaa'

def test_is_response_valid():
    assert chatbot_response(response) == response
