from config.users import STANDARD_USER, STANDARD_PASSWORD


class LoginPage:
    def __init__(self, page):
        self.page = page

    def enter_username(self, username):
        self.page.locator("#user-name").fill(username)

    def enter_password(self, password):
        self.page.locator("#password").fill(password)

    def click_login(self):
        self.page.locator("#login-button").click()
