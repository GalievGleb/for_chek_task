import allure
from pages.base_page import BasePage
from locators.login_page_locators import EMAIL_SELECTOR, PASSWORD_SELECTOR, LOGIN_BUTTON_SELECTOR
from utils.helpers import USERNAME

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'login'

    @allure.step("Авторизация пользователя: {username}")
    def login(self, username, password):
        """
        Выполняет авторизацию пользователя на сайте.
        Процесс авторизации:
        1. Переход на страницу логина
        2. Заполнение поля username
        3. Заполнение поля password
        4. Клик по кнопке входа
        5. Проверка успешной авторизации по наличию текста
        """
        with allure.step("Открываем страницу логина"):
            self.navigate_to()

        with allure.step("Вводим username"):
            self.wait_for_selector_and_fill(EMAIL_SELECTOR, username)

        with allure.step("Вводим password"):
            self.wait_for_selector_and_fill(PASSWORD_SELECTOR, password)

        with allure.step("Нажимаем кнопку входа"):
            self.wait_for_selector_and_click(LOGIN_BUTTON_SELECTOR)

        with allure.step("Проверяем успешную авторизацию"):
            self.assert_text_present_on_page(f"{USERNAME}'s Workspace", 100000)

    @allure.step("Негативная авторизация пользователя: {username}")
    def invalid_login(self, username, password):
        """
        Пытаемся авторизоваться с неверными данными и проверяем сообщение об ошибке
        """
        with allure.step("Открываем страницу логина"):
            self.navigate_to()

        with allure.step("Вводим username"):
            self.wait_for_selector_and_fill(EMAIL_SELECTOR, username)

        with allure.step("Вводим password"):
            self.wait_for_selector_and_fill(PASSWORD_SELECTOR, password)

        with allure.step("Нажимаем кнопку входа"):
            self.wait_for_selector_and_click(LOGIN_BUTTON_SELECTOR)

        with allure.step("Проверяем сообщение об ошибке некорректного пароля"):
            self.assert_text_present_on_page(
                "Incorrect password for this email.",
                100000
            )
