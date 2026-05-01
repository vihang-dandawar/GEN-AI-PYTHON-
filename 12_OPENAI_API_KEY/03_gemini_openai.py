from dotenv import load_dotenv

load_dotenv()


from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyBO-MZFWZjl9Zp34kK8oJe-zetHD8pyyVc",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role":"user",
            "content":"Hey there im vikki Nice to  meet you"}
        
    ]
    
)

print(response.choices[0].message.content)