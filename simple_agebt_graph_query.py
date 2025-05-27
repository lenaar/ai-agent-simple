import re
from typing import Union, Dict
from simple_agent_langgraph import build_graph
from simple_agent_tools import known_skills

def skills_query_graph(agent, question):
    if question.lower() in ["quit", "exit", "bye", "goodbye"]:
        print("Goodbye!")
        return
        
    # Format the question as a proper message state
    messages_state = {
        "messages": [
            {"role": "user", "content": question}
        ]
    }
    
    # Stream the response
    for event in agent.stream(messages_state):
        for value in event.values():
            latest_message = value["messages"][-1]
            # Handle AIMessage object
            if hasattr(latest_message, 'content'):
                print("Assistant:", latest_message.content)
            else:
                print("Assistant: no content found")
    
    # Get next question from main.py
    return