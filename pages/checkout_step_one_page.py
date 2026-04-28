class CheckoutStepOnePage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator("text=Checkout: Your Information")
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")

    def is_checkout_step_one_page_opened(self):
        return self.title.is_visible()

    def enter_first_name(self, value):
        self.first_name_input.fill(value)

    def enter_last_name(self, value):
        self.last_name_input.fill(value)

    def enter_postal_code(self, value):
        self.postal_code_input.fill(value)

    def click_continue_button(self):
        self.continue_button.click()
