
import streamlit as st
from agent import call_agent

st.title("Todo AI Assistant")
st.write("Manage your tasks using AI.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# Take user input
query = st.chat_input("Ask me to manage your todos...")

if query:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    with st.chat_message("user"):
        st.write(query)

    try:
        # Get AI response
        answer = call_agent(query)

        # Display AI response
        with st.chat_message("assistant"):
            st.write(answer)

        # Save AI response
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        st.error(f"Something went wrong: {e}")







# from agent import call_agent


# while True:
#     query = input("you: ")

#     if query.lower().strip() == 'exit':
#         break

#     if not query.strip():
#         continue

#     try:

#         answer = call_agent(query)

#         print(answer)

#     except Exception as e:
#         print("Somethiing went wrong :", e)


