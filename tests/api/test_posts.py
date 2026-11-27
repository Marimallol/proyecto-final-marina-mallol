import pytest


@pytest.mark.api
def test_get_existing_post(api):
    response = api.request("get", "/posts/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert {"userId", "title", "body"} <= response.json().keys()


@pytest.mark.api
@pytest.mark.negative
def test_missing_post_returns_not_found(api):
    response = api.request("get", "/posts/99999")

    assert response.status_code == 404
    assert response.json() == {}


@pytest.mark.api
def test_create_post_echoes_submitted_fields(api):
    payload = {"title": "automation check", "body": "sample body", "userId": 1}
    response = api.request("post", "/posts", json=payload)

    assert response.status_code == 201
    assert {key: response.json()[key] for key in payload} == payload
