import pytest
from unittest.mock import Mock, patch
from simple_agent import SimpleAgent

@pytest.fixture
def mock_openai():
    with patch('simple_agent.openai') as mock:
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Mock response"
        mock.chat.completions.create.return_value = mock_response
        yield mock

class TestSimpleAgent:
    def test_agent_provides_response(self, mock_openai):
        """Test that agent returns a response when asked a question"""
        agent = SimpleAgent()
        response = agent("What is the capital of France?")
        assert response == "Mock response"

    def test_agent_uses_correct_model(self, mock_openai):
        """Test that agent uses the specified model"""
        custom_model = "any-openai-model"
        agent = SimpleAgent(model_name=custom_model)
        agent("Hello")
        
        mock_openai.chat.completions.create.assert_called_once()
        call_args = mock_openai.chat.completions.create.call_args[1]
        assert call_args['model'] == custom_model

    def test_agent_uses_system_prompt(self, mock_openai):
        """Test that agent includes system prompt in the conversation"""
        custom_prompt = "You are a helpful math tutor."
        agent = SimpleAgent(system_prompt=custom_prompt)
        agent("What is 2+2?")
        
        messages = mock_openai.chat.completions.create.call_args[1]['messages']
        assert messages[0]['role'] == 'system'
        assert messages[0]['content'] == custom_prompt

    def test_agent_maintains_conversation_context(self, mock_openai):
        """Test that agent maintains context across multiple interactions"""
        agent = SimpleAgent()
        
        # First interaction
        agent("My name is Alice")
        
        # Second interaction
        agent("What's my name?")
        second_call_messages = mock_openai.chat.completions.create.call_args[1]['messages']
        
        # Verify that the conversation history includes both messages in correct order
        user_messages = [msg['content'] for msg in second_call_messages if msg['role'] == 'user']
        assert len(user_messages) == 2
        assert user_messages[0] == "My name is Alice"
        assert user_messages[1] == "What's my name?"

    def test_agent_handles_empty_system_prompt(self, mock_openai):
        """Test that agent works correctly without a system prompt"""
        agent = SimpleAgent(system_prompt="")
        agent("Hello")
        
        call_args = mock_openai.chat.completions.create.call_args[1]
        messages = call_args['messages']
        assert not any(msg['role'] == 'system' for msg in messages)

    def test_agent_uses_temperature(self, mock_openai):
        """Test that agent uses the correct temperature setting"""
        agent = SimpleAgent()
        agent("Hello")
        
        call_args = mock_openai.chat.completions.create.call_args[1]
        assert call_args['temperature'] == 0.0  # Verify deterministic setting
