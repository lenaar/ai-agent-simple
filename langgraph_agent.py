import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph_agent_tools import tools
from typing import Annotated, TypedDict
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()

openai = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-4.1-nano", temperature=0.0)
# to invoke the model with tools use more complex query, like "find a hotel near Manhatten in New York"
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
        {"role": "user", "content": "find a hotel near Manhatten in New York"}
        ]
    }
    """
    print(state["messages"])

    return {"messages": [model_with_tools.invoke(state["messages"])]}


def build_graph_agent(checkpointer):
    # Initialize the graph
    graph = StateGraph(MessagesState)
    graph.add_node("agent", simple_agent_langgraph)

# Set the entry point - where the graph begins
    graph.set_entry_point("agent")

    # add tools node
    tool_node = ToolNode(tools=tools)
    graph.add_conditional_edges("agent", tools_condition)
    graph.add_node("tools", tool_node)

    # STEP 5: Compile the graph
    return graph.compile(checkpointer=checkpointer)

