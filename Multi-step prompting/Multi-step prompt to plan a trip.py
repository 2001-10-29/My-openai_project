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

# Create a multi-step prompt
prompt = """
I need to plan a 2-week beach vacation.

Step 1: Suggest four potential beach locations.
Step 2: For each location, provide accommodation options and activities.
Step 3: Evaluate the pros and cons of each location.

Present the answer clearly.
"""

# Get response
response = get_response(prompt)

print(response)