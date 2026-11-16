from langchain_nimble import NimbleSearchTool
from langchain.tools import tool
import os
from dotenv import load_dotenv
load_dotenv()
import requests



search_tool = NimbleSearchTool(
    k = 5,
    deep_search = True,
    parsing_type="markdown"
)


@tool
def google_search(query:str):
    """
    Seach anything on google for real time information.
    Args:
        query -> user search query for google search

    return -> result from google  search
    """
    res = search_tool.invoke(query)
    return res


def weather_tool(city:str):
    """
    get real time weather details like tempperature, humidity and others
    Args:
        city -> city name for weatheer details

    return -> weather data from the api response.
    """
    API_URL=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('WEATHER_API_KEY')}&units=metric"
    
    res = requests.get(API_URL)
    if res.status_code == 200:
        return res.json()
    return "Error: Unable to fetch weather data. Please check the city name and try again."

ALL_TOOLS = [google_search, weather_tool]







