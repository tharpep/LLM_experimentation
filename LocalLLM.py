from openai import OpenAI

import re


"""
For terminal usage, run ollama run deepseek-r1:1.b

For or API usage, run ollama serve
"""


client = OpenAI(api_key="not-needed", base_url="http://localhost:11434/v1")

stay = True

while stay:
    inp = input("\nPlease input query(Type /leave to leave): ")

    if inp == "/leave":
        stay = False
    else:
        response = client.chat.completions.create(
            model="deepseek-r1:1.5b",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": inp},
            ],
            stream=False
        )

        full_response =  response.choices[0].message.content
        match = re.search(r'</think>(.*)', full_response, re.DOTALL)
        out = match.group(1).strip() if match else full_response

        print(out)
        