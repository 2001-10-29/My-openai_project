import os
from dotenv import load_dotenv
from openai import OpenAI

#load environment variables from .env
load_dotenv()

# get API key 
api_key = os.getenv("OPENAI_API_KEY")

#Create OpenAI client 
client = OpenAI(api_key=api_key) 

# Craft a prompt that follows the instructions
prompt = "____"

# Get the response
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": prompt}
  ]
)

print(response)