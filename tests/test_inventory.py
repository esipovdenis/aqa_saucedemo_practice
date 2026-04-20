from config.users import STANDARD_USER, STANDARD_PASSWORD
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_inventory(page):
    login_page = LoginPage(page)
    login_page.enter_username(STANDARD_USER)
    login_page.enter_password(STANDARD_PASSWORD)
    login_page.click_login()
    inventory_page = InventoryPage(page)
    assert inventory_page.get_title().is_visible()