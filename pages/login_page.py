from asyncio import timeout

import allure

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
    with allure.step('Данные для входа'):
        mail_input = '#login-email-input'
        password_input = '#login-password-input'
        button_log_in = '.login-page-v4_submit'
        url = 'https://app.clickup.com/login'
    with allure.step('Функция для входа'):
        def login(self, email, password):
            self.go_to('https://app.clickup.com/login')
            self.wait_for(self.mail_input)
            self.wait_for(self.password_input)
            self.fill(self.mail_input, email)
            self.fill(self.password_input, password)
            self.click(self.button_log_in)