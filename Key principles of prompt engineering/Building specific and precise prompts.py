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
        temperature=0.8
    )
    return response.choices[0].message.content

# Create a sample story
story = """In a quiet village surrounded by mountains, there lived a young girl named Eliza who loved adventure. One day, she discovered a hidden path behind her house that she had never seen before."""

# Create a prompt (f-string + triple backticks + instructions)
prompt = f"""Complete the story delimited by triple backticks.
Write only two paragraphs and use the style of Shakespeare.

```{story}```
"""

# Get the generated response
response = get_response(prompt)

# Print results
print("\nOriginal story:\n", story)
print("\nGenerated story:\n", response)