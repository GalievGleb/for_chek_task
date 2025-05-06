import allure
import pytest
from pages.login_page import LoginPage
from utils.helpers import CLICKUP_EMAIL, CLICKUP_PASSWORD


@allure.feature("Login UI Tests")
@allure.story("Успешная авторизация пользователя")
@allure.title("Проверка успешного входа пользователя")
def test_login(browser):
    """
    Тест для проверки успешной авторизации через UI
    """
    page = browser.new_page()
    login_page = LoginPage(page)

    with allure.step("Авторизация с корректными данными"):
        login_page.login(CLICKUP_EMAIL, CLICKUP_PASSWORD)


@allure.feature("Login UI Tests")
@allure.story("Негативная авторизация пользователя")
@allure.title("Проверка ошибки при вводе неверного пароля")
def test_fail_login(browser):
    """
    Тест для проверки отображения ошибки при неверном пароле
    """
    page = browser.new_page()
    login_page = LoginPage(page)

    with allure.step("Попытка входа с некорректным паролем"):
        login_page.invalid_login(CLICKUP_EMAIL, '12345678')
