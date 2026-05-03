from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_items = self.page.locator(".cart_item")
        self.checkout_button = self.page.locator("#checkout")
        self.continue_shopping_button = self.page.locator("#continue-shopping")

    # def get_cart_items(self):
    #     return self.cart_items

    def get_cart_items_count(self):
        return self.cart_items.count()

    def click_checkout_button(self):
        self.checkout_button.click()

    def click_continue_shopping(self):
        self.continue_shopping_button.click()

