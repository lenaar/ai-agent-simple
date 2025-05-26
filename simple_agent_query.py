import re
from typing import Union, Dict
from simple_agent import SimpleAgent
from simple_agent_tools import known_skills

# Match 'Execute:' followed by word chars, then ':' and non-whitespace chars
skills_pattern = re.compile(r"Execute:\s*(\w+):\s*(\S+)")

def parse_skills(response: str) -> dict[str, str]:
    """
    find all matches of the pattern: "Execute: calculate: 2+2 Execute: planet_mass: Earth"
    [("calculate", "2+2"), ("planet_mass", "Earth")]
    return: {"calculate": "2+2", "planet_mass": "Earth"}
    """
    matches = skills_pattern.findall(response)
    return {skill: arg for skill, arg in matches}
    
def skills_query(agent: SimpleAgent, question: str, max_turns: int = 20) -> Union[str, Dict[str, str]]:
    next_prompt = question

    for _ in range(max_turns):
        response = agent(next_prompt)
        print(response)
        skills = parse_skills(response)

        if not skills:
            return
        
        skill, arg = list(skills.items())[0]
        
        if skill not in known_skills:
            raise ValueError(f"Unknown skill: {skill}")
            
        # Execute skill via known_skills
        learning = known_skills[skill](arg)
        next_prompt = f"Learn: {learning}"
        print("Learn:", learning)

    return
