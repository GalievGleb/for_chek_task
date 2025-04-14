from playwright.sync_api import Page
from module_5_playwright.pages.base_page import BasePage
from module_5_playwright.pages.locators.checkout_step_two_locators import *


class CheckoutStepTwoPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._endpoint = '/checkout-step-two.html'

    def click_finish(self) -> None:
        """Завершает оформление заказа, нажав на кнопку 'Finish'."""
        self.wait_for_selector_and_click(FINISH_BUTTON)
