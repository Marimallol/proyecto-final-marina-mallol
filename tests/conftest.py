import base64
from collections.abc import Iterator
from datetime import datetime
from html import escape
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


def _capture_browser_diagnostics(driver: WebDriver, item) -> list:
    diagnostics_dir = PROJECT_ROOT / "reports" / "diagnostics"
    diagnostics_dir.mkdir(parents=True, exist_ok=True)
    safe_name = "".join(
        char if char.isalnum() or char in "-_" else "_" for char in item.name
    )
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    stem = f"{timestamp}_{safe_name}"
    report_extras = []

    try:
        current_url = driver.current_url
    except Exception as exc:  # noqa: BLE001 - diagnostics must not mask test failures
        current_url = f"<could not read current_url: {exc}>"

    try:
        page_source = driver.page_source
    except Exception as exc:  # noqa: BLE001 - diagnostics must not mask test failures
        page_source = f"<!-- Could not read page_source: {escape(str(exc))} -->"

    url_file = diagnostics_dir / f"{stem}.txt"
    url_file.write_text(f"Current URL: {current_url}\n", encoding="utf-8")
    html_file = diagnostics_dir / f"{stem}.html"
    html_file.write_text(page_source, encoding="utf-8")

    report_extras.append(extras.text(current_url, name="Browser current_url"))
    report_extras.append(
        extras.html(
            f'<a href="diagnostics/{html_file.name}">Captured page HTML</a>'
            f' · <a href="diagnostics/{url_file.name}">Current URL details</a>'
        )
    )

    screenshot = diagnostics_dir / f"{stem}.png"
    try:
        if driver.save_screenshot(str(screenshot)):
            encoded = base64.b64encode(screenshot.read_bytes()).decode("ascii")
            report_extras.append(extras.png(encoded, name=screenshot.name))
    except Exception:  # noqa: BLE001 - diagnostics must not mask test failures
        pass

    return report_extras


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.extras = getattr(report, "extras", [])
    if report.when != "call" or not report.failed:
        return

    driver = next(
        (
            item.funcargs.get(name)
            for name in ("browser", "signed_in_browser")
            if item.funcargs.get(name) is not None
        ),
        None,
    )
    if driver is None:
        return

    try:
        report.extras.extend(_capture_browser_diagnostics(driver, item))
    except Exception:  # noqa: BLE001 - diagnostics must not mask test failures
        pass
