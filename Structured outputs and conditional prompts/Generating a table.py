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

# Define function
def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content

# Create a prompt that generates the table
prompt = """
Generate a table of 10 must-read science fiction books.

Requirements:
- Include columns: Title, Author, Year
- Format the output clearly as a table
- Choose popular and highly recommended books
"""

# Get the response
response = get_response(prompt)

print(response)