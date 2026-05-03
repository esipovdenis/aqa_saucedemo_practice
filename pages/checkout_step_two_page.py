from pages.base_page import BasePage
from pages.base_page import BasePage

class CheckoutStepTwoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title =self.page.locator("text=Checkout: Overview")
        self.items = self.page.locator(".cart_item")
        self.finish_button = self.page.locator("#finish")

    def is_checkout_step_two_page_opened(self):
        return self.title.is_visible()

    def get_items_count(self):
        return self.items.count()

    def click_finish_button(self):
        self.finish_button.click()


