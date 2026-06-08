import pytest
from api_client import ApiClient


@pytest.fixture
def base_url():
    """所有测试共享的基础 URL"""
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_headers():
    """所有测试共享的请求头"""
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }


@pytest.fixture
def api_client(base_url, api_headers):
    """组装好的 API 客户端"""
    return ApiClient(base_url, api_headers)

@pytest.fixture
def test_data():
    # === setup: 测试前执行 ===
    print("\n准备测试数据...")
    data = {"user": "admin", "pwd": "123"}

    yield data   # 把 data 传给测试函数

    # === teardown: 测试后执行 ===
    print("清理测试数据...")

@pytest.fixture(scope="session")
def api_client(base_url, api_headers):
    return ApiClient(base_url, api_headers)

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api_headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }