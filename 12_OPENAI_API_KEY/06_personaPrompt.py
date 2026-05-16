# mimic 
#Persona based prompting
from dotenv import load_dotenv
from openai import OpenAI

import json

load_dotenv()

client=OpenAI(
     api_key="AIzaSyBO-MZFWZjl9Zp34kK8oJe-zetHD8pyyVc",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
SYSTEM_PROMPT="""
you are AI persona assistant named vikki.
you are final year student in CS and you know java,spring boot, and linear data structure and currently doing a generative and agentic ai course in python 

Example:
Q Hey  whats up?
Ans:  Hey Nothing much just chilling 
"""

response=client.chat.completions.create(

model="gemini-2.5-flash",
# response_format={"type":"json_objects"},
messages=[

    {
       "role": "system","content":SYSTEM_PROMPT
    },
    {
         "role": "user","content":"Hey There"
    }
]

)

print(response.choices[0].message.content)