import requests


class ApiClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {}

    def get(self, path):
        url = f"{self.base_url}{path}"
        return requests.get(url, headers=self.headers)

    def post(self, path, body):
        url = f"{self.base_url}{path}"
        return requests.post(url, json=body, headers=self.headers)