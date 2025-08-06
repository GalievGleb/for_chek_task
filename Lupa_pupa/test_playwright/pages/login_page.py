from for_chek_task.Lupa_pupa.test_playwright.pages.base_page import BasePage
from for_chek_task.Lupa_pupa.test_playwright.locators import LoginSelectors


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, username, password):
        """ Открывает базовый URL и авторизовывается

        args:
            username: логин
            password: пароль
        """
        self.navigate_to()
        self.wait_for_selector_and_fill(LoginSelectors.USERNAME_SELECTOR, username)
        self.wait_for_selector_and_fill(LoginSelectors.PASSWORD_SELECTOR, password)
        self.wait_for_selector_and_click(LoginSelectors.BUTTON_LOGIN_SELECTOR)
        self.assert_text_present_on_page('Products')