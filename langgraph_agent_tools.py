import os
from typing import Optional
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

# def tool_tavily_search(query: str) -> str:
#     """Search the internet for information about a topic. Use this when you need real-time or factual information.
    
#     Args:
#         query (str): The search query to look up
#     """
#     tavily = TavilySearchResults(max_results=5)
#     return tavily.invoke(query)


tool_tavily_search = TavilySearchResults(max_results=5)
tools = [tool_tavily_search]


# tavily = tool_tavily_search()
# res = tavily.invoke("What is the capital of France?")
# print(res)