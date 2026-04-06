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

# Refine the following prompt
prompt = """
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
Time flies like an arrow -> no explicit emotion

They sat and ate their meal -> Neutral
"""

response = get_response(prompt)
print(response)