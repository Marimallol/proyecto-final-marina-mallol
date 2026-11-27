"""Shopping cart page actions."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions

from qa_automation.pages.base import BasePage


class CartPage(BasePage):
    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    CHECKOUT = (By.ID, "checkout")

    def item_names(self) -> list[str]:
        return [item.text for item in self.driver.find_elements(*self.ITEM_NAMES)]

    def remove(self, product_id: str) -> None:
        self.click((By.CSS_SELECTOR, f"[data-test='remove-{product_id}']"))
        self.wait.until(
            conditions.invisibility_of_element_located(
                (By.CSS_SELECTOR, f"[data-test='remove-{product_id}']")
            )
        )

    def checkout(self) -> None:
        self.click(self.CHECKOUT)
