"""Small HTTP client shared by API tests."""
import logging
from typing import Any

import requests

from qa_automation.settings import settings

logger = logging.getLogger(__name__)


class ApiClient:
    def __init__(
        self,
        base_url: str = settings.api_base_url,
        timeout: int = settings.api_timeout,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout
        self._session = requests.Session()

    def request(self, method: str, endpoint: str, **kwargs: Any) -> requests.Response:
        url = f"{self._base_url}/{endpoint.lstrip('/')}"
        logger.info("%s %s", method.upper(), url)
        response = self._session.request(
            method, url, timeout=self._timeout, **kwargs
        )
        logger.info("HTTP %s", response.status_code)
        return response

    def close(self) -> None:
        self._session.close()
