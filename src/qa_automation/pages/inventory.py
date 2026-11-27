"""Product listing page actions."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from qa_automation.pages.base import BasePage


class InventoryPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "[data-test='title']")
    SORT_MENU = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def is_open(self) -> bool:
        return self.text(self.HEADER) == "Products"

    def add(self, product_id: str) -> None:
        self.click((By.CSS_SELECTOR, f"[data-test='add-to-cart-{product_id}']"))

    def sort(self, option: str) -> None:
        Select(self.wait.until(
            lambda driver: driver.find_element(*self.SORT_MENU)
        )).select_by_visible_text(option)

    def prices(self) -> list[float]:
        return [
            float(element.text.replace("$", ""))
            for element in self.driver.find_elements(*self.PRICES)
        ]

    def open_cart(self) -> None:
        self.click(self.CART_LINK)
