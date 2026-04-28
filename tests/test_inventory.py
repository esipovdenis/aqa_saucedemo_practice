import pytest
from config.users import STANDARD_USER, STANDARD_PASSWORD
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_tc_inv_001_products_count(logged_in_inventory_page):
    """Отображение всех 6 товаров"""
    assert logged_in_inventory_page.get_inventory_items_count() == 6


def test_tc_inv_002_product_names(logged_in_inventory_page):
    """Проверка названий всех товаров"""
    names = logged_in_inventory_page.get_inventory_name()
    assert len(names) > 0


def test_tc_inv_003_product_price(logged_in_inventory_page):
    """Проверка цен всех товаров"""
    prices = logged_in_inventory_page.get_inventory_price()
    assert len(prices) > 0


def test_tc_inv_004_inventory_images(logged_in_inventory_page):
    """Проверка изображений товаров"""
    images = logged_in_inventory_page.get_inventory_images()
    for i in range(images.count()):
        image = images.nth(i)
        assert logged_in_inventory_page.is_image_loaded(image)


def test_tc_inv_005_sort_price_low_to_high(logged_in_inventory_page):
    """Сортировка по цене (низкая → высокая)"""
    logged_in_inventory_page.select_sort_low_to_high()
    prices = logged_in_inventory_page.get_inventory_price()
    numeric_prices = [float(p.replace("$", "")) for p in prices]
    assert numeric_prices == sorted(numeric_prices)


def test_tc_inv_006_sort_price_high_to_low(logged_in_inventory_page):
    """Сортировка по цене (высокая → низкая)"""
    logged_in_inventory_page.select_sort_high_to_low()
    prices = logged_in_inventory_page.get_inventory_price()
    numeric_prices = [float(p.replace("$", "")) for p in prices]
    assert numeric_prices == sorted(numeric_prices, reverse=True)


def test_tc_inv_007_sort_name_a_to_z(logged_in_inventory_page):
    """Сортировка по названию (A→Z)"""
    logged_in_inventory_page.select_sort_a_to_z()
    names = logged_in_inventory_page.get_inventory_name()
    assert names == sorted(names)


def test_tc_inv_008_item_not_lost_after_sort_change(logged_in_inventory_page):
    """Фильтрация после добавления в корзину"""
    logged_in_inventory_page.click_add_to_button()
    assert logged_in_inventory_page.is_button_remove_visible()
    logged_in_inventory_page.select_sort_low_to_high()
    assert logged_in_inventory_page.is_button_remove_visible()


def test_tc_inv_009_click_product_image(logged_in_inventory_page):
    """Клик по изображению товара (если есть переход)"""
    logged_in_inventory_page.click_first_product_image()
    assert "/inventory-item.html?id=" in logged_in_inventory_page.page.url


def test_tc_inv_010_remove_button_after_add_to_cart(logged_in_inventory_page):
    """Проверка кнопки 'Remove' после добавления в корзину"""
    logged_in_inventory_page.click_add_to_button()
    assert logged_in_inventory_page.is_button_remove_visible()
    logged_in_inventory_page.click_remove_button()
    assert not logged_in_inventory_page.is_cart_badge_visible()
