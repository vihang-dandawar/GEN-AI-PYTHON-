from  typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from openrouter import OpenRouter
import os
from langchain_core.messages import AIMessage
from dotenv import load_dotenv
load_dotenv()

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


def samplenode(state:State):
        print(f"\n\ncurrently in  sample node . state info {state}")

        return { "messages":["this is samplenode "]}

graph_builder=StateGraph(State)



graph_builder.add_node("chatnode",chat)
graph_builder.add_node("samplenode",samplenode)

graph_builder.add_edge(START,"chatnode")
graph_builder.add_edge("chatnode","samplenode")
graph_builder.add_edge("samplenode",END)

graph=graph_builder.compile()

updatedState=graph.invoke(State({"messages":["hi my name is vihang "]}))
print(f"updated state {updatedState}")




