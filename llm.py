from langchain_ollama import ChatOllama

from config import MODEL_NAME
from config import TEMPERATURE


llm = ChatOllama(
    model=MODEL_NAME,
    temperature=TEMPERATURE
)
