import pytest
from pages.cart_page import CartPage
from config.users import STANDARD_USER, PROBLEM_USER, STANDARD_PASSWORD
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_tc_cart_001_add_one_product(logged_in_inventory_page):
    """Добавление одного товара"""
    logged_in_inventory_page.click_add_to_cart("Sauce Labs Backpack")
    badge = logged_in_inventory_page.get_cart_badge_text()
    assert badge == "1", "Бейдж корзины должен быть равен 1"


def test_tc_cart_002_add_multiple_products(logged_in_inventory_page):
    """Добавление нескольких разных товаров"""
    logged_in_inventory_page.click_add_to_cart("Sauce Labs Bike Light")
    logged_in_inventory_page.click_add_to_cart("Sauce Labs Bolt T-Shirt")
    logged_in_inventory_page.click_add_to_cart("Sauce Labs Fleece Jacket")
    badge = logged_in_inventory_page.get_cart_badge_text()
    assert badge == "3", "Бейдж корзины должен быть равен 3"


def test_tc_cart_003_add_same_product_twice(logged_in_inventory_page):
    """Добавление одного товара несколько раз"""
    logged_in_inventory_page.click_add_to_cart("Sauce Labs Backpack")
    assert (
        logged_in_inventory_page.get_cart_badge_text() == "1"
    ), "Повторное добавление того же товара не должно увеличивать бейдж"
    assert (
        logged_in_inventory_page.is_button_remove_visible()
    ), "Кнопка Remove должна отображаться после добавления товара"


def test_tc_cart_004_remove_product_from_cart(logged_in_inventory_page):
    """Удаление товара из корзины"""
    logged_in_inventory_page.click_add_to_cart("Sauce Labs Bike Light")
    assert logged_in_inventory_page.get_cart_badge_text() == "1", \
        "Бейдж корзины должен быть равен 1"
    logged_in_inventory_page.click_remove_from_cart("Sauce Labs Bike Light")
    assert not logged_in_inventory_page.is_cart_badge_visible(), \
        "Бейдж корзины не должен отображаться после удаления товара"


@pytest.mark.skip(reason="No quantity controls (+/-) on SauceDemo")
def test_tc_cart_005_change_quantity():
    """Изменение количества товара (если есть +/-)"""
    pass


def test_tc_cart_006_open_cart_page(logged_in_inventory_page):
    """Переход в корзину с любой страницы"""
    logged_in_inventory_page.click_cart_button()
    assert (
        logged_in_inventory_page.is_cart_page_opened()
    ), "Страница корзины не открылась"


def test_tc_cart_007_continue_shopping_returns_to_inventory(
        logged_in_inventory_page):
    """Возврат к покупкам из корзины"""
    logged_in_inventory_page.click_cart_button()
    assert (
        logged_in_inventory_page.is_cart_page_opened()
    ), "Страница inventory не открылась после Continue Shopping"
    cart_page = CartPage(logged_in_inventory_page.page)
    cart_page.click_continue_shopping()
    assert (
        logged_in_inventory_page.is_inventory_page_opened()
    ), "Страница корзины не открылась"


def test_tc_cart_008_empty_cart(logged_in_inventory_page):
    """Пустая корзина: отображение сообщения"""
    logged_in_inventory_page.click_cart_button()
    assert (
        logged_in_inventory_page.is_cart_page_opened()
    ), "Страница корзины не открылась"
    cart_page = CartPage(logged_in_inventory_page.page)
    count = cart_page.get_cart_items_count()
    assert count == 0, "Корзина должна быть пустой"


def test_tc_cart_009_refresh_page_keeps_items(logged_in_inventory_page):
    """Сохранение корзины после перезагрузки"""
    logged_in_inventory_page.click_add_to_cart("Sauce Labs Bike Light")
    assert (
        logged_in_inventory_page.get_cart_badge_text() == "1"
    ), "Бейдж корзины должен быть равен 1"
    logged_in_inventory_page.page.reload()
    assert (
        logged_in_inventory_page.get_cart_badge_text() == "1"
    ), "Бейдж корзины должен быть равен 1"


def test_tc_cart_010_cart_is_empty_for_different_user(page):
    """Корзина при смене пользователя"""
    login_page = LoginPage(page)
    login_page.login_procedure(STANDARD_USER, STANDARD_PASSWORD)
    assert "/inventory.html" in page.url, "После логина не открылась страница inventory"
    inventory_page = InventoryPage(page)
    inventory_page.click_add_to_cart("Sauce Labs Bike Light")
    assert (
        inventory_page.get_cart_badge_text() == "1"
    ), "Бейдж корзины должен быть равен 1"
    new_page = inventory_page.open_new_page("https://www.saucedemo.com/")
    login_page_2 = LoginPage(new_page)
    login_page_2.login_procedure(PROBLEM_USER, STANDARD_PASSWORD)
    inventory_page_2 = InventoryPage(new_page)
    assert (
        not inventory_page_2.is_cart_badge_visible()
    ), "Корзина другого пользователя должна быть пустой"
