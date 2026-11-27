"""Login page actions and state."""
from selenium.webdriver.common.by import By

from qa_automation.pages.base import BasePage
from qa_automation.settings import settings


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self) -> "LoginPage":
        self.driver.get(settings.ui_base_url)
        return self

    def sign_in(self, username: str, password: str) -> None:
        self.enter(self.USERNAME, username)
        self.enter(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def error_message(self) -> str:
        return self.text(self.ERROR)
