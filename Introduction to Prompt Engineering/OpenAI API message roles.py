import os   
from dotenv import load_dotenv
from openai import OpenAI 

#load environment variables from .env
load_dotenv()

# Get API key 
api_key = os.getenv("OPENAI_API_KEY") 

#create openai client
client = OpenAI(api_key=api_key)

# Define the conversation messages
conversation_messages = [
    {"role": "system", "content": "You are a helpful event management assistant."},
    {"role": "user", "content": "What are some good conversation starters at networking events?"},
    {"role": "assistant", "content": "I am preparing event for my friend merrage"}
]

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=conversation_messages
)
print(response.choices[0].message.content)
