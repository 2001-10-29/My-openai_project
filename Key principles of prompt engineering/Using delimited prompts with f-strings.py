import os 
from dotenv import load_dotenv
from openai import OpenAI 

#load environment variables from .env
load_dotenv()

# get api key 
api_key = os.getenv("OPENAI_API_KEY")

#Create OpenAI client
client = OpenAI(api_key=api_key) 

# Sample story (you can change this)
story = """Once upon a time, in a small village, there was a young boy who dreamed of becoming a great explorer. One day, he found a mysterious map hidden in an old book."""

# Create a prompt that completes the story
prompt = f"""Complete the story delimited by triple backticks. 
 ```{story}```"""

# Get the generated response 
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": prompt}
  ]
)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)
