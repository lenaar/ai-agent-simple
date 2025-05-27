from simple_agent import SimpleAgent
from simple_agent_prompt import system_prompt
from simple_agent_tools import known_skills
from simple_agent_query import skills_query
from langgraph_agent import build_graph_agent
from langgraph_agent_query import skills_query_graph
from langgraph_agent_memory import get_checkpointer

def main():
    agent_type = input("Enter agent type (simple_agent or simple_agent_langgraph): ")
    
    if agent_type == "simple_agent_langgraph":
        with get_checkpointer() as checkpointer:
            agent = build_graph_agent(checkpointer)
            while True:
                question = input("\nYour question (or 'quit' to exit): ")
                if question.lower() in ["quit", "exit", "bye", "goodbye"]:
                    print("Goodbye!")
                    break
                skills_query_graph(agent, question)
    else:
        agent = SimpleAgent(system_prompt=system_prompt)
        question = input("Enter your question about planets mass. Example: What is the combined mass of Jupiter and Saturn? \n Your question: ")
        max_turns = int(input("Enter max turns 5-15: "))
        skills_query(agent, question, max_turns)


if __name__ == "__main__":
    main()
