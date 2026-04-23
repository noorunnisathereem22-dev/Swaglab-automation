from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import *

def test_end_to_end_flow(page):

    # Login
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(VALID_USER, VALID_PASSWORD)

    # Inventory
    inventory_page = InventoryPage(page)
    assert inventory_page.is_inventory_loaded()

    inventory_page.add_first_product_to_cart()
    inventory_page.go_to_cart()

    # Cart
    cart_page = CartPage(page)
    assert cart_page.is_item_in_cart()

    cart_page.click_checkout()

    # Checkout
    checkout_page = CheckoutPage(page)
    checkout_page.fill_checkout_details(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout_page.finish_order()

    # Validation
    assert "Thank you for your order!" in checkout_page.get_success_message()