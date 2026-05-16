import os
import json
import requests
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

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
# Async Query Processor
# ---------------------------
async def process_query(query: str):
    print("Searching Chunks:", query)

    # Search in Qdrant
    search_results = vector_store.similarity_search(query=query)

    # Build Context
    context = "\n\n\n".join([
        f"Page Content: {result.page_content}\n"
        f"Page Number: {result.metadata['page_label']}\n"
        f"File Location: {result.metadata['source']}"
        for result in search_results
    ])

    # Prompt
    SYSTEM_PROMPT = f"""
You are a helpful AI Assistant who answers user queries
based only on the available context retrieved from a PDF file.

Guide the user to the correct page number if needed.

Context:
{context}
"""

    # API Key
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    # API Request
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
                    "content": query
                }
            ]
        })
    )

    # Response Output
    result = response.json()

    print(result)

    if "choices" in result:
        print("\n🤖:", result["choices"][0]["message"]["content"])
    else:
        print("\n❌ API Error:", result)
    return result

