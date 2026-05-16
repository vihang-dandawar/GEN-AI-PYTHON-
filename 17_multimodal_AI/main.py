from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# Read your image file
image_path = "photo.png"   # change filename
with open(image_path, "rb") as f:
    image_data = base64.b64encode(f.read()).decode("utf-8")

# Ask model for one-line caption
response = client.chat.completions.create(
    model="openai/gpt-5-mini",   # cheaper vision-capable text model if available
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Create a stylish one-line caption for this image."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_data}"
                    }
                }
            ]
        }
    ],
    max_tokens=50
)

print(response.choices[0].message.content)