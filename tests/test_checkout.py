from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage
import pytest
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage


def test_tc_check_001_successful_checkout(logged_in_inventory_page):
    """Успешное оформление заказа"""
    logged_in_inventory_page.click_add_to_cart("Sauce Labs Backpack")
    assert logged_in_inventory_page.get_cart_badge_text() == "1", \
        "Бейдж корзины должен быть равен 1"

    logged_in_inventory_page.click_cart_button()
    assert logged_in_inventory_page.is_cart_page_opened(), \
        "Страница корзины не открылась"

    cart_page = CartPage(logged_in_inventory_page.page)
    assert cart_page.get_cart_items_count() == 1, \
        "В корзине должен быть 1 товар"

    cart_page.click_checkout_button()

    checkout_step_one_page = CheckoutStepOnePage(logged_in_inventory_page.page)
    assert checkout_step_one_page.is_checkout_step_one_page_opened(), \
        "Страница Checkout Step One не открылась"

    checkout_step_one_page.fill_checkout_form("John", "Doe", "12345")

    checkout_step_two_page = CheckoutStepTwoPage(logged_in_inventory_page.page)
    assert checkout_step_two_page.is_checkout_step_two_page_opened(), \
        "Страница Checkout Overview не открылась"

    assert checkout_step_two_page.get_items_count() == 1, \
        "В overview должен быть 1 товар"

    checkout_step_two_page.click_finish_button()

    checkout_complete_page = CheckoutCompletePage(
        logged_in_inventory_page.page)
    assert checkout_complete_page.is_checkout_complete_opened(), \
        "Страница завершения заказа не открылась"

    assert checkout_complete_page.is_order_completed(), \
        "Сообщение об успешном заказе не отображается"

@pytest.mark.parametrize(
     "first_name, last_name, postal_code, expected_error",
        [
            ("", "Doe", "12345", "Error: First Name is required"),
            ("John", "", "12345", "Error: Last Name is required"),
            ("John", "Doe", "", "Error: Postal Code is required"),
        ],
)
def test_tc_check_002_003_004_required_fields(
    logged_in_inventory_page,
    first_name,
    last_name,
    postal_code,
    expected_error,
):
    """Чекаут с пустым First name"""
    """Чекаут с пустым Last name"""
    """Чекаут с пустым Postal code"""

    logged_in_inventory_page.click_add_to_cart("Sauce Labs Backpack")
    assert logged_in_inventory_page.get_cart_badge_text() == "1", \
        "Бейдж корзины должен быть равен 1"
    logged_in_inventory_page.click_cart_button()
    assert logged_in_inventory_page.is_cart_page_opened(), \
        "Страница корзины не открылась"
    cart_page = CartPage(logged_in_inventory_page.page)
    cart_page.click_checkout_button()
    checkout_step_one_page = CheckoutStepOnePage(logged_in_inventory_page.page)
    assert checkout_step_one_page.is_checkout_step_one_page_opened(), \
        "Страница Checkout Step One не открылась"
    checkout_step_one_page.fill_checkout_form(first_name, last_name, postal_code)
    assert checkout_step_one_page.get_error_message_text() == expected_error, \
        "Некорректное сообщение об ошибке"

def test_tc_check_005_postal_code_format(logged_in_inventory_page):
    """Проверка, что Postal Code принимает любой формат"""
    logged_in_inventory_page.click_add_to_cart("Sauce Labs Backpack")
    assert logged_in_inventory_page.get_cart_badge_text() == "1", \
        "Бейдж корзины должен быть равен 1"
    logged_in_inventory_page.click_cart_button()
    assert logged_in_inventory_page.is_cart_page_opened(), \
        "Страница корзины не открылась"
    cart_page = CartPage(logged_in_inventory_page.page)
    cart_page.click_checkout_button()
    checkout_step_one_page = CheckoutStepOnePage(logged_in_inventory_page.page)
    assert checkout_step_one_page.is_checkout_step_one_page_opened(), \
        "Страница Checkout Step One не открылась"
    checkout_step_one_page.fill_checkout_form("John", "Doe", "abcde")
    checkout_step_two_page = CheckoutStepTwoPage(logged_in_inventory_page.page)
    assert checkout_step_two_page.is_checkout_step_two_page_opened(), \
        "Переход на Step Two не произошёл — поле Postal Code валидируется"

