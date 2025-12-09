# load imports
from typing import TypedDict,Annotated
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph , START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage , HumanMessage, AIMessage

# llm loading
load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.2)

# State Loading
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]

# Build the graph
graph = StateGraph(ChatState)
checkpoint = MemorySaver()


def chat_node(state:ChatState):
    input = state['messages']
    message = llm.invoke(input)
    return {'messages': [message]}
    


graph.add_node('chat_node',chat_node)

graph.add_edge(START,'chat_node');
graph.add_edge('chat_node',END);

Chatbot = graph.compile(checkpointer=checkpoint)