class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.postal_code = "#postal-code"
        self.continue_button = "#continue"
        self.finish_button = "#finish"
        self.success_msg = ".complete-header"

    def fill_checkout_details(self,first, last, zip_code):
        self.page.fill(self.first_name, first) 
        self.page.fill(self.last_name, last)
        self.page.fill(self.postal_code, zip_code)
        self.page.click(self.continue_button)

      
    def finish_order(self):
        self.page.click(self.finish_button)

    def get_success_message(self):
        return self.page.locator(self.success_msg).text_content()
