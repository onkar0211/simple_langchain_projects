from langchain.agents import create_agent
from langchain_groq import ChatGroq
from tools import ALL_TOOLS
import os
from dotenv import load_dotenv
load_dotenv()



def get_agent():
    "Get Agent with google searchh and weatheer search abilities"

    return create_agent(
        model=ChatGroq(model="openai/gpt-oss-20b"),
        tools=ALL_TOOLS,
        system_prompt=(
            "You are a research assistant with google search and weather tools.\n"
            "Use 'google_search' for quick search on google"
            "for deep research that may take several minutes."
            "If user is looking for weather details like temperature, humidity or any other details"
            "then call the 'weather_tool' to get the real time weather data"
        )
    )


