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

# Sample text (more than one sentence)
text = """Technology is changing the way we live and work. It helps businesses grow and improves communication across the world."""

# Create the instructions
instructions = (
    "Determine the language of the given text and count the number of sentences it contains. "
    "If the text has more than one sentence, generate a suitable title for it. "
    "If the text has only one sentence, write 'N/A' for the title. "
    "The text will be provided inside triple backticks.\n\n"
)

# Create the output format
output_format = (
    "Output format:\n"
    "Text:\n"
    "Language:\n"
    "Number of sentences:\n"
    "Title:\n\n"
)

# Create the final prompt
prompt = instructions + output_format + f"```{text}```"

# Get the response
response = get_response(prompt)

print(response)