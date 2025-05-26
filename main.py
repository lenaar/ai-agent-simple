from simple_agent import SimpleAgent
from simple_agent_prompt import system_prompt
from simple_agent_tools import known_skills
from simple_agent_query import skills_query

def main():
    # Initialize the agent with custom prompt
    agent = SimpleAgent(system_prompt=system_prompt)
    

    question = "What is the combined mass of Jupiter and Saturn?"

    skills_query(agent, question)


if __name__ == "__main__":
    main()
