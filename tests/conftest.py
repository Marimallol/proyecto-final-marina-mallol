import base64
from collections.abc import Iterator
from datetime import datetime
from pathlib import Path

import pytest
from pytest_html import extras
from selenium.webdriver.remote.webdriver import WebDriver

from qa_automation.api import ApiClient
from qa_automation.browser import create_driver
from qa_automation.pages.login import LoginPage

PROJECT_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def browser() -> Iterator[WebDriver]:
    driver = create_driver()
    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def signed_in_browser(browser: WebDriver) -> WebDriver:
    LoginPage(browser).open().sign_in("standard_user", "secret_sauce")
    return browser


@pytest.fixture
def api() -> Iterator[ApiClient]:
    client = ApiClient()
    try:
        yield client
    finally:
        client.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.extras = getattr(report, "extras", [])
    if report.when != "call" or not report.failed:
        return

    driver = item.funcargs.get("browser") or item.funcargs.get("signed_in_browser")
    if driver is None:
        return

    screenshot_dir = PROJECT_ROOT / "reports" / "screenshots"
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    safe_name = "".join(
        char if char.isalnum() or char in "-_" else "_" for char in item.name
    )
    filename = f"{datetime.now():%Y%m%d_%H%M%S}_{safe_name}.png"
    screenshot = screenshot_dir / filename
    driver.save_screenshot(str(screenshot))
    encoded = base64.b64encode(screenshot.read_bytes()).decode("ascii")
    report.extras.append(extras.png(encoded, name=filename))
