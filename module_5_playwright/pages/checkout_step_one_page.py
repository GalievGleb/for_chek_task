from playwright.sync_api import Page
from module_5_playwright.pages.base_page import BasePage
from module_5_playwright.pages.locators.checkout_step_one_locators import *


class CheckoutStepOnePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._endpoint = '/checkout-step-one.html'

    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму оформления заказа на первом шаге.

            first_name (str): Имя.
            last_name (str): Фамилия.
            postal_code (str): Почтовый индекс.
        """
        self.wait_for_selector_and_fill(FIRST_NAME_SELECTOR, first_name)
        self.wait_for_selector_and_fill(LAST_NAME_SELECTOR, last_name)
        self.wait_for_selector_and_fill(POSTAL_CODE_SELECTOR, postal_code)

    def click_continue(self) -> None:
        """Нажимает на кнопку 'Continue' для перехода ко второму шагу подтверждения покупки."""
        self.wait_for_selector_and_click(CONTINUE_BUTTON)
