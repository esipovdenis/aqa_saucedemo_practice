import pytest
from playwright.sync_api import sync_playwright
from config.base import URL_BASE


@pytest.fixture()
def page(request):
    """Фикстура для инициализации страницы браузера"""
    headless_mode = getattr(request, "param", False)
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=headless_mode, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        page.goto(URL_BASE)

        yield page


        browser.close()