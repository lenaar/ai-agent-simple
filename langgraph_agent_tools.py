from langchain.tools import StructuredTool
from langchain_community.tools.tavily_search import TavilySearchResults
from typing import Optional

# Initialize Tavily search with proper schema
tool_tavily_search = StructuredTool.from_function(
    func=TavilySearchResults(max_results=5).invoke,
    name="tavily_search",
    description="Search the internet for current information. Use this for questions about recent events, facts, or any information that might need up-to-date data.",
    return_direct=True
)

# List of available tools
tools = [tool_tavily_search]