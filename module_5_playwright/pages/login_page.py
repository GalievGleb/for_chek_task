from playwright.sync_api import Page
from module_5_playwright.pages.base_page import BasePage
from module_5_playwright.pages.locators.login_locators import *


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._endpoint = ''

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход пользователя по указанным логину и паролю.

        username (str): Имя пользователя.
        password (str): Пароль пользователя.
        """
        self.navigate_to()
        self.wait_for_selector_and_fill(USERNAME_SELECTOR, username)
        self.wait_for_selector_and_fill(PASSWORD_SELECTOR, password)
        self.wait_for_selector_and_click(LOGIN_BUTTON)
        self.assert_text_present_on_page('Products')
