from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage, SystemMessage
import streamlit as st

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")

history = []



# history.append(SystemMessage(content="You are very arrogant, bad, toxic AI assistant who always gives false information"))

# while True:
#     query = input("Ask Question: ")
#     if query == 'exit':
#         break
#     history.append(HumanMessage(content=query))
#     res = llm.invoke(history)

#     answer = res.content
#     history.append(AIMessage(content=answer))
#     print(answer)


import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Toxic AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e1b4b, #312e81);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 800;
    background: linear-gradient(90deg, #a78bfa, #67e8f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
}

[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 15px;
    padding: 12px;
    margin-bottom: 12px;
}

[data-testid="stChatInput"] {
    border: 1px solid #818cf8;
    border-radius: 15px;
}

.stButton button {
    background: linear-gradient(90deg, #7c3aed, #4f46e5);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: bold;
}

.stButton button:hover {
    border: 1px solid #a78bfa;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# Initialize LLM
@st.cache_resource
def get_llm():
    return ChatGroq(model="openai/gpt-oss-20b")

llm = get_llm()


# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = [
        SystemMessage(
            content="You are a sarcastic assistant. You may use playful sarcasm, but always provide accurate information."
        )
    ]


# Header
st.markdown(
    '<div class="main-title">🤖 Toxic AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your brutally sarcastic AI companion.</div>',
    unsafe_allow_html=True
)


# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    st.write("Conversation controls")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.history = [
            SystemMessage(
                content="You are a sarcastic assistant. You may use playful sarcasm, but always provide accurate information."
            )
        ]
        st.rerun()

    st.divider()
    st.caption("Powered by LangChain + Groq")


# Display previous messages
for message in st.session_state.history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user", avatar="🧑"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(message.content)


# Chat input
query = st.chat_input("Ask something...")

if query:
    # Display user message
    with st.chat_message("user", avatar="🧑"):
        st.markdown(query)

    # Store user message
    st.session_state.history.append(HumanMessage(content=query))

    # Generate response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("AI is thinking..."):
            try:
                response = llm.invoke(st.session_state.history)
                answer = response.content

                st.markdown(answer)

                # Store AI response
                st.session_state.history.append(
                    AIMessage(content=answer)
                )

            except Exception as e:
                st.error(f"Something went wrong: {e}")
