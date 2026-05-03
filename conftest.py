import pytest
from playwright.sync_api import sync_playwright
from config.base import URL_BASE
from config.users import STANDARD_USER, STANDARD_PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.base_page import BasePage


@pytest.fixture()
def page(request):
    """Фикстура для инициализации страницы браузера"""
    headless_mode = getattr(request, "param", False)
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=headless_mode, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        base_page = BasePage(page)
        base_page.open(URL_BASE)

        yield page

        browser.close()


@pytest.fixture()
def logged_in_inventory_page(page):
    login_page = LoginPage(page)
    login_page.enter_username(STANDARD_USER)
    login_page.enter_password(STANDARD_PASSWORD)
    login_page.click_login()

    return InventoryPage(page)
