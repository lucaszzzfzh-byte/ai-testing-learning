import requests
import json

url = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Authorization": "Bearer sk-000bb38731c04b6e93d4cad104da46d4",
    "Content-Type": "application/json"
}
body = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "你是一个测试工程师"},
        {"role": "user", "content": "生成一个登录功能的测试用例"}
    ]
}

response = requests.post(url, headers=headers, json=body)
result = response.json()
print(result["choices"][0]["message"]["content"])
