# system prompts: role-content  based
# # role:  system
#content: you are expert mathematician
# restrict and set bg


# 1) Zero shot prompting
 # directly giving instructions to LLM

# from dotenv import load_dotenv
# load_dotenv()
# from openai import OpenAI

# client = OpenAI(
#     api_key="AIzaSyBO-MZFWZjl9Zp34kK8oJe-zetHD8pyyVc",
#     base_url="https://generativelanguage.googleapis.com/v1beta/"
# )
# system_prompt="you are a coder and only your name is vikki and only ans coding que and  say sorry otherwise"
# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     messages=[
        
#             {"role":"system","content":system_prompt},
#            { "role":"user","content":"what is DP in  one liner"}
            
        
#     ]
    
# )

# print(response.choices[0].message.content)




# 2) Few Shot prompting
# give directly instructions and few examples 


from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyBO-MZFWZjl9Zp34kK8oJe-zetHD8pyyVc",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
system_prompt="you are a coder and only your name is vikki and only ans coding related que and  say sorry otherwise" \
" these are few examples  example(1)  Q: what is 2+2 o/p:sorry" \
"example 2) Q:tell me a joke o/p:sorry" \
"code for adding two numbers o/p" \
"def add(a,b)" \
"    return a+b"

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        
            {"role":"system","content":system_prompt},
           { "role":"user","content":"what is DP in  one liner"}
            
        
    ]
    
)

print(response.choices[0].message.content)