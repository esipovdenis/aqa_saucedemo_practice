import pytest
from pages.cart_page import CartPage
from config.users import STANDARD_USER, PROBLEM_USER, STANDARD_PASSWORD
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_tc_cart_001_add_one_product(inventory_page):
    """Добавление одного товара"""
    inventory_page.click_add_to_cart("Sauce Labs Backpack")
    badge = inventory_page.get_cart_badge_text()
    assert badge == "1"

def test_tc_cart_002_add_multiple_products(inventory_page):
    """Добавление нескольких разных товаров"""
    inventory_page.click_add_to_cart("Sauce Labs Bike Light")
    inventory_page.click_add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.click_add_to_cart("Sauce Labs Fleece Jacket")
    badge = inventory_page.get_cart_badge_text()
    assert badge == "3"

def test_tc_cart_003_add_same_product_twice(inventory_page):
    """Добавление одного товара несколько раз"""
    inventory_page.click_add_to_cart("Sauce Labs Bike Light")
    inventory_page.click_add_to_cart("Sauce Labs Bike Light")
    badge = inventory_page.get_cart_badge_text()
    assert badge == "1"


def test_tc_cart_004_remove_product_from_cart(inventory_page):
    """Удаление товара из корзины"""
    inventory_page.click_add_to_cart("Sauce Labs Bike Light")
    assert inventory_page.get_cart_badge_text() == "1"
    inventory_page.click_remove_from_cart("Sauce Labs Bike Light")
    assert not inventory_page.is_cart_badge_visible()

@pytest.mark.skip(reason="No quantity controls (+/-) on SauceDemo")
def test_tc_cart_005_change_quantity():
    """Изменение количества товара (если есть +/-)"""
    pass

def test_tc_cart_006_open_cart_page(inventory_page):
    """Переход в корзину с любой страницы"""
    inventory_page.click_cart_button()
    assert inventory_page.is_cart_page_opened()


def test_tc_cart_007_continue_shopping_returns_to_inventory(inventory_page):
    """Возврат к покупкам из корзины"""
    inventory_page.click_cart_button()
    assert inventory_page.is_cart_page_opened()
    cart_page = CartPage(inventory_page.page)
    cart_page.click_continue_shopping()
    assert inventory_page.is_inventory_page_opened()


def test_tc_cart_008_empty_cart(inventory_page):
    """Пустая корзина: отображение сообщения"""
    inventory_page.click_cart_button()
    assert inventory_page.is_cart_page_opened()
    cart_page = CartPage(inventory_page.page)
    count = cart_page.get_cart_items_count()
    assert count == 0

def test_tc_cart_009_refresh_page_keeps_items(inventory_page):
    """Сохранение корзины после перезагрузки"""
    inventory_page.click_add_to_cart("Sauce Labs Bike Light")
    assert inventory_page.get_cart_badge_text() == "1"
    inventory_page.page.reload()
    assert inventory_page.get_cart_badge_text() == "1"


def test_tc_cart_010_cart_is_empty_for_different_user(page):
    """Корзина при смене пользователя"""
    login_page = LoginPage(page)
    login_page.enter_username(STANDARD_USER)
    login_page.enter_password(STANDARD_PASSWORD)
    login_page.click_login()
    assert "/inventory.html" in page.url
    inventory_page = InventoryPage(page)
    inventory_page.click_add_to_cart("Sauce Labs Bike Light")
    assert inventory_page.get_cart_badge_text() == "1"
    new_context = page.context.browser.new_context()
    new_page = new_context.new_page()
    new_page.goto("https://www.saucedemo.com/")
    login_page_2 = LoginPage(new_page)
    login_page_2.enter_username(PROBLEM_USER)
    login_page_2.enter_password(STANDARD_PASSWORD)
    login_page_2.click_login()
    inventory_page_2 = InventoryPage(new_page)
    assert not inventory_page_2.is_cart_badge_visible()

    new_context.close()

