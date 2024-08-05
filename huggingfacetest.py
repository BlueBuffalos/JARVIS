from huggingface_hub import InferenceClient
from config import HF_TOKEN

client = InferenceClient(
    "microsoft/Phi-3-mini-4k-instruct",
    token=HF_TOKEN,
)

while True:
    chat = input("\nYou: ")
    for message in client.chat_completion(
    messages=[{"role": "user", "content": chat}],
    max_tokens=500,
    stream=True,
    ):
      print(message.choices[0].delta.content, end="")
