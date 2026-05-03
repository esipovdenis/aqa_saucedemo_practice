from pages.base_page import BasePage
class CheckoutStepOnePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title = self.page.locator("text=Checkout: Your Information")
        self.first_name_input = self.page.locator("#first-name")
        self.last_name_input = self.page.locator("#last-name")
        self.postal_code_input = self.page.locator("#postal-code")
        self.continue_button = self.page.locator("#continue")
        self.first_name = self.page.locator('#first-name')
        self.error_message = self.page.locator("[data-test='error']")


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

    def fill_checkout_form(self,first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue_button()

    def get_error_message_text(self):
        return self.error_message.inner_text()
