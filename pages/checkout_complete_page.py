from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title = self.page.locator("text=Checkout: Complete!")
        self.success_message = self.page.locator("text=Thank you for your order!")

    def is_checkout_complete_opened(self):
        return self.title.is_visible()

    def is_order_completed(self):
        return self.success_message.is_visible()
