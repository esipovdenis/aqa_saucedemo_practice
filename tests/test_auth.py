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
    ERR_MSG_WRONG_DATA,
    ERR_MSG_USER_REQUIRED,
    ERR_MSG_PASS_REQUIRED,
    ERR_MSG_LOCKED_OUT,
)


@pytest.mark.parametrize("user", [STANDARD_USER, PROBLEM_USER, PERFORMANCE_GLITCH_USER])
def test_login(page, user):
    """Успешный вход со стандартным пользователем / Успешный вход с другими валидными пользователями"""
    login_page = LoginPage(page)
    login_page.login_procedure(user, STANDARD_PASSWORD)
    assert "/inventory.html" in page.url
    assert login_page.is_products_header_visible()


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (STANDARD_USER, INVALID_PASSWORD, ERR_MSG_WRONG_DATA),
        (INVALID_USER, STANDARD_PASSWORD, ERR_MSG_WRONG_DATA),
        ("", STANDARD_PASSWORD, ERR_MSG_USER_REQUIRED),
        (STANDARD_USER, "", ERR_MSG_PASS_REQUIRED),
        (LOCKED_OUT_USER, STANDARD_PASSWORD, ERR_MSG_LOCKED_OUT),
    ],
)
def test_login_negative(page, username, password, expected_error):
    """Групповой тест всех негативных сценариев (неверные данные, пустые поля, блокировка)"""
    login_page = LoginPage(page)
    login_page.login_procedure(username, password)
    assert expected_error in login_page.get_error_message_text()
