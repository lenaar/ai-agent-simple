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

print(response.choices[0].message.content)




