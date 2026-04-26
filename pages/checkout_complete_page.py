class CheckoutCompletePage:
    def __init__(self, page):
        self.page = page


    def is_checkout_complete_opened(self):
        return self.page.locator("text=Checkout: Complete!").is_visible()

    def is_order_completed(self):
       return self.page.locator("text=Thank you for your order!").is_visible()
