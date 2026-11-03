import os
from openai import OpenAI

client = OpenAI()

MODEL = os.environ.get("OPENAI_MODEL","gpt-4.1-mini")

response = client.responses.create(
    model=MODEL,
    input = "What is a neural network in one sentence?",
    max_output_tokens=100
)

print("SDK response:",response.output_text)
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
