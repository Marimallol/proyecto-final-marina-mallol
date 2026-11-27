from unittest.mock import Mock, patch

import pytest
import requests

from qa_automation.api import ApiClient


def test_api_request_uses_joined_url_and_timeout():
    response = Mock(status_code=200)
    with patch("qa_automation.api.requests.Session") as session_factory:
        session = session_factory.return_value
        session.request.return_value = response
        client = ApiClient("https://api.example/", timeout=4)

        result = client.request("get", "/posts/1")

        session.request.assert_called_once_with(
            "get", "https://api.example/posts/1", timeout=4
        )
        assert result is response
        client.close()
        session.close.assert_called_once_with()


def test_api_request_propagates_timeout():
    with patch("qa_automation.api.requests.Session") as session_factory:
        session = session_factory.return_value
        session.request.side_effect = requests.Timeout("request timed out")
        client = ApiClient("https://api.example", timeout=1)

        with pytest.raises(requests.Timeout, match="request timed out"):
            client.request("get", "/posts/1")

        client.close()
