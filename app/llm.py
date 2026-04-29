import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("MODEL", "gpt-5.3")


def llm_call(messages, temperature=0.7):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content
