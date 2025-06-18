from clickup.pages.base_page import BasePage
from clickup.helpers.utils import USER_NAME
import allure

@allure.feature("Функционал авторизации")
class LoginPage(BasePage):
    EMAIL_INPUT_SELECTOR = '#login-email-input'
    PASSWORD_INPUT_SELECTOR = '#login-password-input'
    LOGIN_BUTTON_SELECTOR = 'button >> span:has-text("Log In")'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'login'

    @allure.step("Выполнить вход в систему")
    def login(self, username: str, password: str):
        with allure.step("Открыть страницу логина"):
            self.navigate_to()
        with allure.step("Ввести email пользователя"):
            self.wait_for_selector_and_fill(self.EMAIL_INPUT_SELECTOR, username)
        with allure.step("Ввести пароль"):
            self.wait_for_selector_and_type(self.PASSWORD_INPUT_SELECTOR, password, 200)
        with allure.step("Нажать кнопку 'Log In'"):
            self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)
        with allure.step("Проверить успешную авторизацию"):
            self.assert_text_is_on_page(f"{USER_NAME}'s Workspace", 100000)


    @allure.step("Попытка входа с невалидными данными")
    def invalid_login(self, username: str, password: str):
        with allure.step("Открыть страницу логина"):
            self.navigate_to()
        with allure.step("Ввести некорректный email"):
            self.wait_for_selector_and_fill(self.EMAIL_INPUT_SELECTOR, username)
        with allure.step("Ввести некорректный пароль"):
            self.wait_for_selector_and_type(self.PASSWORD_INPUT_SELECTOR, password, 200)
        with allure.step("Нажать кнопку 'Log In'"):
            self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)
        with allure.step("Проверить сообщение об ошибке"):
            self.assert_text_is_on_page("Incorrect password", 100000)
