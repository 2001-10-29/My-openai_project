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

# Create the chain-of-thought prompt
prompt = """
Solve the following problem step by step and explain your reasoning.

Step 1: My friend is 20 years old.
Step 2: My friend's father is twice my friend's age.
Step 3: Calculate the father's current age.
Step 4: Calculate the father's age in 10 years.

What will be the father's age in 10 years?
"""

response = get_response(prompt)
print(response)