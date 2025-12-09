import streamlit as st
from langchain_core.messages import HumanMessage

from chatbot_backend import Chatbot

st.title("Chatbot")

# this is to maintain the contextual memory of llm
thread_id = 1
config = {'configurable': {'thread_id': thread_id}}

# this is to maintain the chat history in the frontend
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

for message in st.session_state['message_history']:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type your message here")


if user_input:

    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message("user"):
        st.markdown(user_input)


    response = Chatbot.invoke({'messages': [HumanMessage(content=user_input)]} , config=config)
    ai_message = response['messages'][-1].content

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.markdown(ai_message)



