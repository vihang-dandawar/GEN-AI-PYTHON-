# LLM-> large language model
# input->input token
# output-> output token
# GPT-> Generative Pre-trained Transformer(type of neural network architecture)
#transformer firstly introduced by google for google translate 
# "Attention is All you need"
# gpt is transformer which takes input token and predict next token & repeat  and hence you get all the output
# 1)  input :hey there-> o/p:I
# 2) input :hey there I-> o/p:am
# 3) input :hey there I am-> o/p:Good
# 4) input :hey there-> o/p:hey there I am Good

# GPU intensive

# converting user input to numbers, 
#  feed to transformer ,
# let transformer generated next set of numbers
#detookenize it
#get outout
#  checkout tiktokenize  to check token for user input
# eg :"You are a helpful assistant" (gpt-4o)

# tokens: <|im_start|>system<|im_sep|
# >You are a helpful assistant<
# |im_end|><|im_start|>user<|im_sep|>
# <|im_end|><|im_start|>assistant<|im_sep|>
# <|im_end|><|im_start|>assistant<|im_sep|>


#200264, 17360, 200266, 3575, 553, 261, 10297, 29186, 200265, 200264, 1428, 200266, 200265, 200264, 173781, 200266, 200265, 200264, 173781, 200266


#Implementing a custom tokenizer

# Activate virtual env
# install tiktoken (package) from openai for tokenize/de text 


import tiktoken 

encoder=tiktoken.encoding_for_model("gpt-4o")

text="hey there! my name is Vihang "
tokens=encoder.encode(text)
print(f"tokens :{tokens}")
tokens :[48467, 1354, 0, 922, 1308, 382, 631, 2431, 516, 220]

decoded_text=encoder.decode(tokens)
print(f"decoder text: {decoded_text}")

# vector_embedding=> gives semantic meaning to tokens
# paris->Eiffel tower  -> India->? (India gate) 
# A computer should be able to interprete this relation for which vector embedding  is used 
# chech out vector embedding map on tensorflow  site


# ---- Positional Embedding-----
#allowing the model to understand sequence context (like "Allen walks dog" vs. "dog walks Allen")

# ----Self Attention
# allows vectors to talk to each others
# 1) River Bank ->  river cha kinara
# 2) ICICI  Bank -> Actual financial bank
# transformers get to know diff between theses tokens















