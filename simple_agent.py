import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

llm_name = "gpt-4.1-nano"

response = openai.chat.completions.create(
    model=llm_name,
    messages=[
        {"role": "system", "content": "You are an intelligent, kind and helpful assistant."},
        {"role": "user", "content": "Hi, where can I book a trip to, so I can enjoy warm beaches in the winter time?"}
    ]
)

#print(response.choices[0].message.content)

# add types to the class
class SimpleAgent:
    def __init__(self, model_name: str = "gpt-4.1-nano", system_prompt: str = "You are an intelligent, kind and helpful assistant."):
        self.model_name = model_name
        self.system_prompt = system_prompt
        self.messages = []
        if system_prompt:
            self.messages.append({"role": "system", "content": system_prompt})

    def __call__(self, user_message: str):
        self.messages.append({"role": "user", "content": user_message})
        assistant_response = self.execute()
        self.messages.append({"role": "assistant", "content": assistant_response})
        return assistant_response
    
    def execute(self) -> str:
        assistant_response = openai.chat.completions.create(
            model=self.model_name,
            temperature=0.0, # 0.0 - deterministic, 1.0 - random (creative)
            messages=self.messages
        )
        return assistant_response.choices[0].message.content