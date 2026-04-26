from config.users import STANDARD_USER, STANDARD_PASSWORD

class LoginPage:
    def __init__(self, page):
        self.page = page
        """Локаторы полей и кнопок"""
        self._username_field = page.locator("#user-name")
        self._password_field = page.locator("#password")
        self._login_button = page.locator("#login-button")

        """Локаторы для проверок (из ассертов)"""
        self._products_header = page.locator("text=Products")
        self._error_msg_container = page.locator(
            ".error-message-container"
        )  # Лучше использовать класс контейнера
        self._error_text = page.locator("text=Epic sadface")

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


# class LoginPage:
#     def __init__(self, page):
#         self.page = page
#
#     def enter_username(self, username):
#         self.page.locator("#user-name").fill(username)
#
#     def enter_password(self, password):
#         self.page.locator("#password").fill(password)
#
#     def click_login(self):
#         self.page.locator("#login-button").click()
