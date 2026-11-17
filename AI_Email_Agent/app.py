
import streamlit as st

from agents import agent
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(
    page_title="AI Email Assistant",
    page_icon="📧",
    layout="centered"
)

st.title("AI Email Assistant")
st.write("Send emails using your LangChain AI Agent.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# User input
query = st.chat_input("Ask me to send an email...")

if query:

    # Add user message
    human_message = HumanMessage(content=query)
    st.session_state.messages.append(human_message)

    with st.chat_message("user"):
        st.write(query)

    # Run AI agent
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            res = agent.invoke({
                "messages": st.session_state.messages
            })

            st.session_state.messages = res["messages"]

            response = st.session_state.messages[-1].content

            st.write(response)










# from agents import agent
# from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# messages=[]

# while True:
#     query=input("\n user: ")
#     if query == 'exit':
#         break

#     messages.append(HumanMessage(content=query))

#     res = agent.invoke({
#         "messages": messages
#     })
#     messages = res["messages"]

#     print(messages[-1].content)







