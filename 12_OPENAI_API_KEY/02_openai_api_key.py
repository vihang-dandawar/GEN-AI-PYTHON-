from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-nano",
    input="Write about me and how is my personality based on my searches."
)

print(response.output_text)