import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from typing import Annotated, TypedDict

load_dotenv()

openai = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-4.1-nano", temperature=0.0)

# state to keep messages
class MessagesState(TypedDict):
    messages: Annotated[list, add_messages]

def simple_agent_langgraph(state: MessagesState):
    """
    Example: state = {
    "messages": [
        {"role": "user", "content": "What's 2+2?"}
        ]
    }
    """
    print(state["messages"])

    return {"messages": [openai.invoke(state["messages"])]}

def build_graph():
    graph = StateGraph(MessagesState, simple_agent_langgraph)
    """
    Start -> simple_agent_langgraph -> END
    """
    graph.add_node("simple_agent_langgraph", simple_agent_langgraph)
    graph.set_entry_point("simple_agent_langgraph")
    graph.set_finish_point("simple_agent_langgraph")
    

    return graph.compile()

graph = build_graph()
result = graph.invoke({"messages": [{"role": "user", "content": "What's 2+2?"}]})
print(result)