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
        temperature=0
    )
    return response.choices[0].message.content

# Create a one-shot prompt
prompt = """
Q: Extract the odd numbers from {1, 3, 7, 12, 19}.
A: Odd numbers = {1, 3, 7, 19}

Q: Extract the odd numbers from {3, 5, 11, 12, 16}.
A: Odd numbers = {3, 5, 11}
"""

# Get the response
response = get_response(prompt)

print(response)