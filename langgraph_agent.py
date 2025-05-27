import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph_agent_tools import tools, BasicToolNode
from typing import Annotated, TypedDict, Literal

load_dotenv()

openai = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-4.1-nano", temperature=0.0)
model_with_tools = openai.bind_tools(tools)

# response = model_with_tools.invoke([{"role": "user", "content": "What is the capital of France?"}])
# print(response)

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

    return {"messages": [model_with_tools.invoke(state["messages"])]}

def route_tools(state: MessagesState) -> Literal["tools", END]:
    """Use the conditional node to route the messages to the correct tool. Otherwise, end the graph."""
    if isinstance(state, list):
        ai_message = state[-1]
    elif messages := state.get("messages", []):
        ai_message = messages[-1]
    else:
        raise ValueError("No messages found in state")
    if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
        return "tools"
    return END
    

def build_graph_agent():
    # Initialize the graph
    graph = StateGraph(MessagesState)
    tool_node = BasicToolNode(tools=tools)
    graph.add_conditional_edges("agent", route_tools, {"tools": "tools", END: END})
    graph.add_node("tools", tool_node)
    # Add the agent node
    graph.add_node("agent", simple_agent_langgraph)
    
    # Set the entry point - where the graph begins
    graph.set_entry_point("agent")
    
    # Set the end point
    # graph.add_edge("agent", END)
    
    # Compile the graph
    return graph.compile()