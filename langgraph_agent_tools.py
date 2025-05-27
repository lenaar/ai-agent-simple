import os
from typing import Optional
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()



tool_tavily_search = TavilySearchResults(max_results=5)
tools = [tool_tavily_search]


# tavily = tool_tavily_search()
# res = tavily.invoke("What is the capital of France?")
# print(res)