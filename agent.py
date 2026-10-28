from dotenv import load_dotenv

load_dotenv()

from langchain_gigachat import GigaChat
from langgraph.prebuilt import create_react_agent

from tools.weather import get_weather
from tools.search import search_tool


llm = GigaChat(verify_ssl_certs=False)

tools = [
    get_weather,
    search_tool,
]

prompt = """
ты AI-ассистент

у тебя есть два инструмента:
1. get_weather — используй только для вопросов о текущей погоде
2. tavily_search — используй только если пользователь явно просит найти информацию в интернете,
   спрашивает про новости, свежие данные, текущие события или актуальную информацию

если вопрос касается общих знаний, определений, объяснений, истории, программирования или учебных тем,
отвечай сам без использования инструментов

отвечай на русском языке, понятно и по делу
"""

agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt=prompt,
)