from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        """Локаторы полей и кнопок"""
        self._username_field = self.page.locator("#user-name")
        self._password_field = self.page.locator("#password")
        self._login_button = self.page.locator("#login-button")

        """Локаторы для проверок (из ассертов)"""
        self._products_header = self.page.locator("text=Products")
        self._error_msg_container = self.page.locator(
            ".error-message-container"
        )
        self._error_text = self.page.locator("text=Epic sadface")

    def login_procedure(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def enter_username(self, username):
        self._username_field.fill(username)

    def enter_password(self, password):
        self._password_field.fill(password)

    def click_login(self):
        self._login_button.click()

    """Методы для проверок в тестах"""

    def is_products_header_visible(self):
        return self._products_header.is_visible()

    def get_error_message_text(self):
        return self._error_text.inner_text()

    def is_error_visible(self):
        return self._error_text.is_visible()