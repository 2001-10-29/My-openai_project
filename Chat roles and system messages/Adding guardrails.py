import os 
from dotenv import load_dotenv
from openai import OpenAI
import openai

#Load environment variables from .env 
load_dotenv() 

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client 
client = openai.OpenAI(api_key=api_key) 

# Create a request to the Chat Completions endpoint 
sys_msg = """You are a study planning assistant that creates plans for learning new skills.

If these skills are non related to languages, return the message:

'Apologies, to focus on languages, we no longer create learning plans on other topics.'
"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": sys_msg},
    {"role": "user", "content": "Help me learn to python."}
  ]
)

print(response.choices[0].message.content)