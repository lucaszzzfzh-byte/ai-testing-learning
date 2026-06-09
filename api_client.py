import requests
class ApiClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {}
        self.session = requests.Session()           # 创建一个持久会话
        self.session.headers.update(self.headers)    # 把 headers 焊进 session

    def get(self, path):
        url = f"{self.base_url}{path}"
        try:
            response = self.session.get(url, timeout=10)   # 用 session 发请求
            return response
        except requests.exceptions.Timeout:
            print(f"请求超时：{url}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"请求失败：{url}，原因：{e}")
            return None

    def post(self, path, body):
        url = f"{self.base_url}{path}"
        try:
            response = self.session.post(url, json=body, timeout=10)
            return response
        except requests.exceptions.Timeout:
            print(f"请求超时：{url}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"请求失败：{url}，原因：{e}")
            return None

# class ApiClient:
#     def __init__(self, base_url, headers=None):
#         self.base_url = base_url
#         self.headers = headers or {}

#     def get(self, path):
#         url = f"{self.base_url}{path}"
#         try:
#             response = requests.get(url, headers=self.headers, timeout=10)
#             return response
#         except requests.exceptions.Timeout:
#             print(f"请求超时：{url}")
#             return None
#         except requests.exceptions.RequestException as e:
#             print(f"请求失败：{url}，原因：{e}")
#             return None

#     def post(self, path, body):
#         url = f"{self.base_url}{path}"
#         try:
#             response = requests.post(url, json=body, headers=self.headers, timeout=10)
#             return response
#         except requests.exceptions.Timeout:
#             print(f"请求超时：{url}")
#             return None
#         except requests.exceptions.RequestException as e:
#             print(f"请求失败：{url}，原因：{e}")
#             return None