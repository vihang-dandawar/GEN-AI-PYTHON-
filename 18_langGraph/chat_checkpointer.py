from  typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from openrouter import OpenRouter
import os
from langchain_core.messages import AIMessage
from dotenv import load_dotenv
load_dotenv()
from langgraph.checkpoint.mongodb import MongoDBSaver


client=OpenRouter(
      api_key=os.getenv("OPENROUTER_API_KEY")
)




class State(TypedDict):
    messages:Annotated[list,add_messages]


def chat(state: State):

    last_message = state["messages"][-1].content

    response = client.chat.send(
        model="openai/gpt-5.4-nano",
        max_tokens=100,
        messages=[
            {
                "role": "user",
                "content": last_message
            }
        ]
    )

    reply = response.choices[0].message.content

    return {
        "messages": [
            AIMessage(content=reply)
        ]
    }




graph_builder=StateGraph(State)



graph_builder.add_node("chatnode",chat)

graph_builder.add_edge(START,"chatnode")
graph_builder.add_edge("chatnode",END)


def compile_Graph_with_checkpointer(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)
       


DB_URL="mongodb://admin:admin@localhost:27017"
with MongoDBSaver.from_conn_string(DB_URL) as checkpointer:
    graph_with_checkpointer=compile_Graph_with_checkpointer(checkpointer=checkpointer)

    config={

"configurable":{
    "thread_id":"vikki"
}
}




    input_data = {
    "messages": ["what is my name"]
}

    for event in graph_with_checkpointer.stream(input_data, config):
    
        for node_name, node_output in event.items():
        
            if "messages" in node_output:
                last_msg = node_output["messages"][-1]
                print(last_msg.content)



