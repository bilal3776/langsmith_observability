from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("LANGSMITH_PROJECT"))
print(os.getenv("GROK_API_KEY"))