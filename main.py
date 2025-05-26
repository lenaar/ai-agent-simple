from simple_agent import SimpleAgent
from simple_agent_prompt import system_prompt
from simple_agent_tools import known_skills
from simple_agent_query import skills_query

def main():
    # Initialize the agent with custom prompt
    agent = SimpleAgent(system_prompt=system_prompt)
    max_turns = int(input("Enter max turns 5-15: "))

    # rewrite question to be interactive with example
    question = input("Enter your question about planets mass. Example: What is the combined mass of Jupiter and Saturn? \n Your question: ")

    skills_query(agent, question, max_turns)


if __name__ == "__main__":
    main()
