class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.inventory_container = ".inventory_list"
        self.add_to_cart_button = "button[data-test*='add-to-cart']"
        self.cart_icon = ".shopping_cart_link"

    def is_inventory_loaded(self):
        return self.page.locator(self.inventory_container).is_visible()

    def add_first_product_to_cart(self):
        self.page.locator(self.add_to_cart_button).first.click()

    def go_to_cart(self):
        self.page.click(self.cart_icon)