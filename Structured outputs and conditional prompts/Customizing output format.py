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

# Create a sample text
text = """Artificial intelligence is transforming industries by improving efficiency,
automating tasks, and enabling smarter decision-making across businesses worldwide."""

# Create the instructions
instructions = (
    "Determine the language of the following text and generate a suitable title for it. "
    "Use the provided output format. The text will be delimited using triple backticks."
)

# Create the output format
output_format = (
    "Text:\n"
    "Language:\n"
    "Title:"
)

# Create the final prompt
prompt = f"""
{instructions}

Output format:
{output_format}

Text to analyze:
```{text}```
"""

# Get the response
response = get_response(prompt)

print(response)