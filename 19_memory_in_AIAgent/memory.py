from mem0 import Memory
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
NEO4J_USERNAME=os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD=os.getenv("NEO4J_PASSWORD")
NEO4J_URI=os.getenv("NEO4J_URI")
# Create OpenRouter client
client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

config = {
    "version": "v1.1",

    "embedder": {
    "provider": "huggingface",
    "config": {
        "model": "sentence-transformers/all-MiniLM-L6-v2"
    }
},

    "llm": {
        "provider": "openai",
        "config": {
            "api_key": OPENROUTER_API_KEY,
            "openai_base_url": "https://openrouter.ai/api/v1",
            "model": "openai/gpt-4.1-mini"
        }
    },

     "graph_store":{
        "provider": "neo4j",
        "config": {
            "url": NEO4J_URI,
            "username": NEO4J_USERNAME,
            "password": NEO4J_PASSWORD
        }
    },

    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
            "collection_name": "hf_collection",
            "embedding_model_dims": 384
        }
    }
}



memory = Memory.from_config(config)


from neo4j import GraphDatabase

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
with driver.session() as session:
    print(session.run("RETURN 1 AS ok").single()["ok"])


while True:
    user_query = input("> ")

    search_result = memory.search(
    query=user_query,
    filters={"user_id": "vikki"}
)

    memories = "\n".join(
    [item["memory"] for item in search_result.get("results", [])]
)

    response = client.chat.completions.create(
    model="openai/gpt-4.1-mini",
    max_tokens=350,
    messages=[
        {
            "role": "system",
            "content": f"Relevant past memories about the user:\n{memories}"
        },
        {
            "role": "user",
            "content": user_query
        }
    ]
)

    ai_response = response.choices[0].message.content

    memory.add(
    user_id="vikki",
    messages=[
        {"role": "user", "content": user_query},
        {"role": "assistant", "content": ai_response}
    ]
)

    print(ai_response)
    print("memory has been saved...")







