import allure
import pytest
from pages.base_page import BasePage
from locators.login_page_locators import USERNAME_SELECTOR, PASSWORD_SELECTOR, LOGIN_BUTTON_SELECTOR


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''
        self.username_selector = USERNAME_SELECTOR
        self.password_selector = PASSWORD_SELECTOR
        self.login_button_selector = LOGIN_BUTTON_SELECTOR


    @allure.step("Авторизация пользователя")
    def login(self, username, password):
        """
        Выполняет авторизацию пользователя на сайте.
    Процесс авторизации:
    1. Переход на страницу логина
    2. Заполнение поля username
    3. Заполнение поля password
    4. Клик по кнопке входа
    5. Проверка успешной авторизации по наличию текста 'Products'
    Args:
        username (str): Логин пользователя
        password (str): Пароль пользователя
        """
        self.navigate_to()
        try:
            self.wait_for_selector_and_fill(self.username_selector, username)
            self.wait_for_selector_and_fill(self.password_selector, password)
            self.wait_for_selector_and_click(self.login_button_selector)
        except Exception as er:
            pytest.fail(f"Ошибка при выходе из аккаунта: {str(er)}")
        self.assert_text_present_on_page('Products')
