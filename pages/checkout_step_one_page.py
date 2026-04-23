class CheckoutStepOnePage:
    def __init__(self, page):
        self.page = page

    def is_checkout_step_one_page_opened(self):
       return self.page.locator("text=Checkout: Your Information").is_visible()

    def enter_first_name(self, value):
        self.page.locator("#first-name").fill(value)

    def enter_last_name(self, value):
        self.page.locator("#last-name").fill(value)

    def enter_postal_code(self, value):
        self.page.locator("#postal-code").fill(value)

    def click_continue_button(self):
        self.page.locator("#continue").click()
