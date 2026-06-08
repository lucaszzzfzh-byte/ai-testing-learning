import pytest


def test_get_post(api_client):
    response = api_client.get("/posts/1")

    assert response.status_code == 200

    data = response.json()
    assert "title" in data


def test_create_post(api_client):
    body = {
        "title": "我的测试帖子",
        "body": "这是内容",
        "userId": 1
    }

    response = api_client.post("/posts", body)

    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["id"] is not None


@pytest.mark.parametrize("post_id,expected_status", [
    (1, 200),
    (2, 200),
    (3, 200),
    (99999, 404),
])
def test_get_post_by_id(api_client, post_id, expected_status):
    response = api_client.get(f"/posts/{post_id}")
    assert response.status_code == expected_status

def test_with_fixture_data(test_data):
    assert test_data["user"] == "admin"
    assert test_data["pwd"] == "123"