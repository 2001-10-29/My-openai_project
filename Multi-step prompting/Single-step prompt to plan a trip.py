import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not found")

# Create client
client = OpenAI(api_key=api_key)

# Define the function
def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=150,  # limits response length (faster)
        temperature=0.7
    )
    return response.choices[0].message.content

# Create a single-step prompt
prompt = "I have 2 weeks of break from my job. Help me plan a beach vacation."

# Get response
response = get_response(prompt)

print(response)