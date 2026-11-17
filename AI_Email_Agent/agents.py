from langchain.agents import create_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from tools import ALL_TOOLS
import os
load_dotenv()

MODEL = os.environ["LLM_MODEL"]

llm = ChatGroq(model=MODEL)

agent = create_agent(
    model=llm,
    tools=ALL_TOOLS,
    system_prompt=
    """
    You are an intelligent email assistant.

    Your responsibilities:

    1. Understand user email requests.
    2. Generate professional email content.
    3. Identify recipient, subject and body.
    4. Use send_email_tool to send emails.
    5. Never claim an email was sent unless
       the tool confirms successful delivery.
    6. If recipient information is missing,
       ask the user for it.
    """
)





