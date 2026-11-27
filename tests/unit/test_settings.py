import pytest

from qa_automation.settings import Settings


def test_settings_read_urls_and_browser_mode(monkeypatch):
    monkeypatch.setenv("UI_BASE_URL", "https://shop.example/")
    monkeypatch.setenv("API_BASE_URL", "https://api.example/")
    monkeypatch.setenv("HEADLESS", "yes")
    monkeypatch.setenv("UI_TIMEOUT", "7")

    config = Settings.from_env()

    assert config.ui_base_url == "https://shop.example"
    assert config.api_base_url == "https://api.example"
    assert config.headless is True
    assert config.ui_timeout == 7


def test_settings_reject_invalid_timeout(monkeypatch):
    monkeypatch.setenv("UI_TIMEOUT", "0")

    with pytest.raises(ValueError, match="UI_TIMEOUT"):
        Settings.from_env()
