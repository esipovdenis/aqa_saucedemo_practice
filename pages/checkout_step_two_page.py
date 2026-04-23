class CheckoutStepTwoPage:
    def __init__(self, page):
        self.page = page

    def is_checkout_step_two_page_opened(self):
        return self.page.locator("text=Checkout: Overview").is_visible()

    def get_items(self):
        return self.page.locator(".cart_item")

    def get_items_count(self):
        items = self.get_items()
        return items.count()

    def click_finish_button(self):
        self.page.locator("#finish").click()


