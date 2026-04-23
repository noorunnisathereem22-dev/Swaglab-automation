class CartPage:

    def __init__(self, page):
        self.page = page
        self.cart_items = ".cart_item"
        self.checkout_button = "#checkout"

    def is_item_in_cart(self):
        return self.page.locator(self.cart_items).count() > 0

    def click_checkout(self):
        self.page.click(self.checkout_button)