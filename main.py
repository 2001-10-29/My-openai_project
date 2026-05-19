import os 
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not found")

def get_response(prompt):
    client = OpenAI(api_key=api_key)
    response= client.chat.completions.create(
        model="gpt-4o-mini",
        max_completion_tokens=100,
        messages= [{"role": "user", "content":prompt}] 
    )
    return response.choices[0].message.content

response = get_response("Explain about the different role,user and system, use bullet points for your response")
print(response) 