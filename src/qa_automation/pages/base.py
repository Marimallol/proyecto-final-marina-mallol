"""Common browser interactions used by page objects."""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait

from qa_automation.settings import settings


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.ui_timeout)

    def click(self, locator: tuple[str, str]) -> None:
        self.wait.until(conditions.element_to_be_clickable(locator)).click()

    def enter(self, locator: tuple[str, str], value: str) -> None:
        element = self.wait.until(conditions.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def text(self, locator: tuple[str, str]) -> str:
        return self.wait.until(
            conditions.visibility_of_element_located(locator)
        ).text
