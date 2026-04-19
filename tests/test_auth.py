import pytest
from pages.login_page import LoginPage

from config.users import (
    STANDARD_USER,
    STANDARD_PASSWORD,
    PROBLEM_USER,
    PERFORMANCE_GLITCH_USER,
    INVALID_PASSWORD,
    INVALID_USER,
    LOCKED_OUT_USER,
)

"""Успешный вход со стандартным пользователем / Успешный вход с другими валидными пользователями"""


@pytest.mark.parametrize("user", [STANDARD_USER, PROBLEM_USER, PERFORMANCE_GLITCH_USER])
def test_login(page, user):
    login_page = LoginPage(page)
    login_page.enter_username(user)
    login_page.enter_password(STANDARD_PASSWORD)
    login_page.click_login()
    assert "/inventory.html" in page.url
    assert page.locator("text=Products").is_visible()


"""Вход с неверным паролем"""


def test_login_invalid_password(page):
    login_page = LoginPage(page)
    login_page.enter_username(STANDARD_USER)
    login_page.enter_password(INVALID_PASSWORD)
    login_page.click_login()
    assert "/inventory.html" not in page.url
    assert page.locator("text=Epic sadface").is_visible()


"""Вход с несуществующим логином"""


def test_login_invalid_username(page):
    login_page = LoginPage(page)
    login_page.enter_username(INVALID_USER)
    login_page.enter_password(STANDARD_PASSWORD)
    login_page.click_login()
    assert "/inventory.html" not in page.url
    assert page.locator("text=Epic sadface").is_visible()


"""Пустой логин"""


def test_login_field_is_blank(page):
    login_page = LoginPage(page)
    login_page.enter_username("")
    login_page.enter_password(STANDARD_PASSWORD)
    login_page.click_login()
    assert "/inventory.html" not in page.url
    assert page.locator("text=Epic sadface: Username is required").is_visible()


"""Пустой пароль"""


def test_password_field_is_blank(page):
    login_page = LoginPage(page)
    login_page.enter_username(STANDARD_USER)
    login_page.enter_password("")
    login_page.click_login()
    assert "/inventory.html" not in page.url
    assert page.locator("text=Epic sadface: Password is required").is_visible()


"""Заблокированный пользователь"""


def test_blocked_user(page):
    login_page = LoginPage(page)
    login_page.enter_username(LOCKED_OUT_USER)
    login_page.enter_password(STANDARD_PASSWORD)
    login_page.click_login()
    assert "/inventory.html" not in page.url
    assert page.locator(
        "text=Epic sadface: Sorry, this user has been locked out."
    ).is_visible()
