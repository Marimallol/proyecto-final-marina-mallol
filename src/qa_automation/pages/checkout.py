"""Checkout flow pages."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions

from qa_automation.pages.base import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def submit_delivery_details(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        self.enter(self.FIRST_NAME, first_name)
        self.enter(self.LAST_NAME, last_name)
        self.enter(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE)
        self.wait.until(conditions.element_to_be_clickable(self.FINISH))

    def place_order(self) -> None:
        self.click(self.FINISH)
        self.wait.until(
            conditions.visibility_of_element_located(self.COMPLETE_HEADER)
        )

    def confirmation(self) -> str:
        return self.text(self.COMPLETE_HEADER)
