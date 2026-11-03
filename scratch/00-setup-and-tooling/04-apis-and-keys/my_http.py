
import os
import json
import urllib.request
from pprint import pprint

# 1. API 주소
url = "https://api.openai.com/v1/responses"

# 2. 인증 정보
api_key = os.environ["OPENAI_API_KEY"]

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

# 3. 요청 본문
body = {
    "model": os.environ.get("OPENAI_MODEL", "gpt-4.1-mini"),
    "input": "What is a neural network in one sentence?",
    "max_output_tokens": 100,
}

# 4. JSON 변환
data = json.dumps(body).encode("utf-8")
print("data :",data)

# 5. HTTP 요청 생성
request = urllib.request.Request(
    url,
    data=data,
    headers=headers,
    method="POST",
)

print("request :",request)

# 6. API 호출
with urllib.request.urlopen(request, timeout=30) as response:
    print("response :", response)
    result = json.loads(response.read())
    
# print("result :",result)
for key, value in result.items():
    print(f"{key}: {value}")

# 7. 출력 텍스트 추출
texts = [
    part.get("text", "")
    for item in result.get("output", [])
    if item.get("type") == "message"
    for part in item.get("content", [])
    if part.get("type") == "output_text"
]

print("Raw HTTP response:", "\n".join(texts))
print("Input tokens:", result["usage"]["input_tokens"])
print("Output tokens:", result["usage"]["output_tokens"])
