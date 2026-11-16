
import streamlit as st
from agents import get_agent
from langchain_core.messages import HumanMessage, AIMessage

# Page configuration
st.set_page_config(
    page_title="AI Search & Weather Assistant",
    page_icon="🤖",
    layout="centered"
)

# Create agent
call_agent = get_agent()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# UI heading
st.title("AI Search & Weather Assistant")
st.caption("Search anything or check weather in any city.")

# Display previous messages
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# Chat input
query = st.chat_input("Ask something...")

if query:

    # Save user message
    st.session_state.messages.append(
        HumanMessage(content=query)
    )

    with st.chat_message("user"):
        st.write(query)

    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            res = call_agent.invoke({
                "messages": st.session_state.messages
            })

            st.session_state.messages = res["messages"]

            answer = res["messages"][-1].content

            st.write(answer)







# from agents import get_agent
# from langchain_core.messages import HumanMessage, AIMessage


# call_agent = get_agent()

# messages = []

# while True:
#     query = input("Search here or ask for weather in any city")
#     if query == 'exit':
#         break

#     messages.append(HumanMessage(content=query))

#     res=call_agent.invoke({
#             "messages":messages
#         })
#     messages = res["messages"]
#     answer=res["messages"][-1].content
    
#     print("AI: ",answer)

