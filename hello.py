import os
import json
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

MODEL = "gpt-3.5-turbo"

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get(os.getenv("OPENAI_API_KEY")),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model=MODEL,
)

print(json.dump(chat_completion, indent=2, ensure_ascii=False))
