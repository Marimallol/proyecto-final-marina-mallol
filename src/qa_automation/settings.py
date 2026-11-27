"""Runtime settings read from environment variables."""
import os
from dataclasses import dataclass


def _read_bool(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    value = raw.strip().lower()
    if value in {"1", "true", "yes", "on"}:
        return True
    if value in {"0", "false", "no", "off"}:
        return False
    raise ValueError(f"{name} must be a boolean value")


def _read_positive_int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None:
        return default
    try:
        value = int(raw)
    except ValueError as exc:
        raise ValueError(f"{name} must be a positive integer") from exc
    if value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


@dataclass(frozen=True)
class Settings:
    ui_base_url: str
    api_base_url: str
    headless: bool
    ui_timeout: int
    api_timeout: int

    @classmethod
    def from_env(cls) -> "Settings":
        ui_url = os.getenv("UI_BASE_URL", "https://www.saucedemo.com").strip()
        api_url = os.getenv(
            "API_BASE_URL", "https://jsonplaceholder.typicode.com"
        ).strip()
        if not ui_url or not api_url:
            raise ValueError("UI_BASE_URL and API_BASE_URL cannot be empty")
        return cls(
            ui_base_url=ui_url.rstrip("/"),
            api_base_url=api_url.rstrip("/"),
            headless=_read_bool("HEADLESS", False),
            ui_timeout=_read_positive_int("UI_TIMEOUT", 10),
            api_timeout=_read_positive_int("API_TIMEOUT", 10),
        )


settings = Settings.from_env()
