import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()  # 直接把返回内容转成字典，等于 json.loads(response.text)

print(f"状态码：{response.status_code}")
print(f"标题：{data['title']}")
print(f"正文：{data['body']}")
# POST 请求 —— 提交数据
data = {"title": "我的测试帖子", "body": "这是内容", "userId": 1}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)
print(f"\nPOST 状态码：{response.status_code}")
print(f"返回的帖子ID：{response.json()['id']}")