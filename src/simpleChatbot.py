import os, sys
from anthropic import Anthropic 

XAI_API_KEY = os.getenv("XAI_API_KEY")
client = Anthropic(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai",
)

def grokOutput(input):
    message = client.messages.create(
        model="grok-beta",
        max_tokens=128,
        system="You are Grok, a chatbot which can explain everything in layman terms, like the user is 5 years old.",
        messages=[
            {
                "role": "user",
                "content": input,
            },
        ],
    )
    print("Grok: " +str(message.content))

while True:
    print("This is laymangrok, it can explain all your queries like you are five years old. Enter 'quit' to exit.")
    inputString = str(input())
    if inputString == "quit":
        sys.exit()
    grokOutput(inputString)


