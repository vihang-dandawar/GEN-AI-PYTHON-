# from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
import requests
import os
import json

# Load env variables
load_dotenv()

# ---------------------------
# Embedding Model
# ---------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------------------
# Connect Existing Qdrant Collection
# ---------------------------
vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_RAG"
)

# ---------------------------
# User Query
# ---------------------------
user_query = input("Ask Something: ")

# ---------------------------
# Similarity Search
# ---------------------------
query_result = vector_store.similarity_search(query=user_query)

# ---------------------------
# Build Context
# ---------------------------
context = "\n\n".join(
    [
        f"Page Content: {result.page_content}\n"
        f"Page Number: {result.metadata.get('page_label')}\n"
        f"File Location: {result.metadata.get('source')}"
        for result in query_result
    ]
)

# ---------------------------
# System Prompt
# ---------------------------
SYSTEM_PROMPT = f"""
You are an expert AI Assistant who answers user queries only from the given context.

If answer is not present in context, say:
"I could not find this in the document."

Context:
{context}
"""

# ---------------------------
# OpenRouter API Key
# ---------------------------
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# ---------------------------
# API Request
# ---------------------------
response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    },
    data=json.dumps({
        "model": "openai/gpt-5.2",
        "max_tokens": 500,
        "temperature": 0.7,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
    })
)
# ---------------------------
# Output
# ---------------------------
result = response.json()

# Debug full response
print(result)

# Check success
if "choices" in result:
    print("\n🤖:", result["choices"][0]["message"]["content"])
else:
    print("\n❌ API Error:", result)