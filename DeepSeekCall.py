from openai import OpenAI

import os

api_key = os.environ['DeepSeek Key']

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")


inp = input("Query:")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": inp},
    ],
    stream=False
)

print(response.choices[0].message.content)