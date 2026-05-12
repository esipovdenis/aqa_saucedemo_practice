from pages.base_page import BasePage
from pages.base_page import BasePage

class CheckoutStepTwoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title =self.page.locator("text=Checkout: Overview")
        self.items = self.page.locator(".cart_item")
        self.finish_button = self.page.locator("#finish")
        self.item_total = self.page.locator(".summary_subtotal_label")
        self.tax = self.page.locator(".summary_tax_label")
        self.total_info = self.page.locator(".summary_total_label")

    def is_checkout_step_two_page_opened(self):
        return self.title.is_visible()

    def get_items_count(self):
        return self.items.count()

    def click_finish_button(self):
        self.finish_button.click()

    def get_item_total(self):
        text = self.item_total.inner_text()
        return float(text.split("$")[1])

    def get_tax(self):
        text = self.tax.inner_text()
        return float(text.split("$")[1])

    def get_total_summary(self):
        text = self.total_info.inner_text()
        return float(text.split("$")[1])

