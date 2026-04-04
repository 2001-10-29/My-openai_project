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
        max_completion_tokens=200,  # keeps it short (may truncate)
        temperature=0.7
    )
    return response.choices[0].message.content

prompt = """
Create a Markdown table listing the top 10 pre-trained language models.
The table must have exactly three columns: 
| Model Name | Release Year | Owning Company |
Ensure each row contains all three pieces of information.
Sort the models by release year from newest to oldest.
Provide concise, accurate, and up-to-date information for each model.
"""
response = get_response(prompt)
print(response)