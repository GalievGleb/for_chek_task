import allure
from pages.base_page import BasePage
from  locators.logout_page_locators import (HEADER_TEXT_SELECTOR, MAIN_TEXT_SELECTOR,
                                            BURGER_BUTTON_SELECTOR, LOGOUT_BUTTON_SELECTOR)
from locators.login_page_locators import LOGIN_BUTTON_SELECTOR


class LogoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-complete.html'
        self.header_text_selector = HEADER_TEXT_SELECTOR
        self.main_text_selector = MAIN_TEXT_SELECTOR
        self.burger_button_selector = BURGER_BUTTON_SELECTOR
        self.logout_button_selector = LOGOUT_BUTTON_SELECTOR
        self.login_button_selector = LOGIN_BUTTON_SELECTOR

    @allure.step("Проверка страницы checkout")
    def check_logout_page(self):
        self.assert_element_is_visible(self.header_text_selector)
        self.assert_text_in_element(self.header_text_selector, 'Checkout: Complete!')
        self.assert_element_is_visible(self.main_text_selector)
        self.assert_text_in_element(self.main_text_selector, 'Thank you for your order!')

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.assert_element_is_visible(self.burger_button_selector)
        self.wait_for_selector_and_click(self.burger_button_selector)
        self.assert_element_is_visible(self.logout_button_selector)
        self.wait_for_selector_and_click(self.logout_button_selector)

        #проверка возврата на начальную страницу
        self.assert_element_is_visible(self.login_button_selector)
