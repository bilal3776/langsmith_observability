from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    groq_api_key=os.getenv("GROK_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

prompt = PromptTemplate.from_template("{question}")
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke(
    {"question": "What is the capital of Peru?"}
)

print(result)