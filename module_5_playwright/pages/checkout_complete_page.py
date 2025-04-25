from playwright.sync_api import Page
from module_5_playwright.pages.base_page import BasePage
from module_5_playwright.pages.locators.checkout_complete_locators import *
from module_5_playwright.pages.locators.login_locators import LOGIN_BUTTON


class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._endpoint = '/checkout-complete.html'

    def checking_order_completion(self):
        """
        Проверяет, что заказ успешно завершён:
        - Отображается заголовок 'Checkout: Complete!'
        - Присутствует благодарственное сообщение
        - Кнопка возврата 'Back Home' видна
        """
        self.assert_element_is_visible(CHECKOUT_TITLE)
        self.assert_text_in_element(CHECKOUT_TITLE, 'Checkout: Complete!')
        self.assert_element_is_visible(THANK_YOU_HEADER)
        self.assert_text_in_element(THANK_YOU_HEADER, 'Thank you for your order!')
        self.assert_element_is_visible(BACK_HOME_BUTTON)

    def logout(self):
        """
        Выполняет выход из аккаунта:
        - Открывает бургер-меню
        - Нажимает на кнопку выхода
        - Проверяет, что отображается кнопка логина
        """
        self.wait_for_selector_and_click(BURGER_ICON)
        self.wait_for_selector_and_click(LOGOUT_BUTTON)
        self.assert_element_is_visible(LOGIN_BUTTON)
