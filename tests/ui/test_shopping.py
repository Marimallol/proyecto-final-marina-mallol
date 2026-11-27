import pytest

from qa_automation.pages.cart import CartPage
from qa_automation.pages.checkout import CheckoutPage
from qa_automation.pages.inventory import InventoryPage

BACKPACK = "sauce-labs-backpack"


@pytest.mark.ui
def test_remove_item_from_cart(signed_in_browser):
    inventory = InventoryPage(signed_in_browser)
    inventory.add(BACKPACK)
    inventory.open_cart()

    cart = CartPage(signed_in_browser)
    assert cart.item_names() == ["Sauce Labs Backpack"]
    cart.remove(BACKPACK)
    assert cart.item_names() == []


@pytest.mark.ui
@pytest.mark.parametrize(
    ("sort_option", "reverse"),
    [
        ("Price (low to high)", False),
        ("Price (high to low)", True),
    ],
)
def test_inventory_price_order(signed_in_browser, sort_option, reverse):
    inventory = InventoryPage(signed_in_browser)
    inventory.sort(sort_option)

    prices = inventory.prices()
    assert prices == sorted(prices, reverse=reverse)


@pytest.mark.ui
def test_complete_purchase(signed_in_browser):
    inventory = InventoryPage(signed_in_browser)
    inventory.add(BACKPACK)
    inventory.open_cart()
    CartPage(signed_in_browser).checkout()

    checkout = CheckoutPage(signed_in_browser)
    checkout.submit_delivery_details("Alex", "Taylor", "10001")
    checkout.place_order()

    assert checkout.confirmation() == "Thank you for your order!"
