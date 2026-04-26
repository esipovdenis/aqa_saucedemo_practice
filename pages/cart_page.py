class CartPage:
    def __init__(self, page):
        self.page = page

    def get_cart_items(self):
        return self.page.locator(".cart_item")


    def get_cart_items_count(self):
        items = self.get_cart_items()
        return items.count()

    def click_checkout_button(self):
        self.page.locator("#checkout").click()

    def click_continue_shopping(self):
        self.page.locator("#continue-shopping").click()

