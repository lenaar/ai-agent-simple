from simple_agent import SimpleAgent
from simple_agent_prompt import system_prompt
from simple_agent_tools import known_skills

def main():
    # Initialize the agent with custom prompt
    agent = SimpleAgent(system_prompt=system_prompt)
    
    response = agent("What is the mass of Mars?")
    print("Assistant:", response)

    response = agent("What is the combined mass of Jupiter and Saturn?")
    print("Assistant:", response)

    


if __name__ == "__main__":
    main()
