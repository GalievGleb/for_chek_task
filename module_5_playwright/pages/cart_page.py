from playwright.sync_api import Page
from module_5_playwright.pages.base_page import BasePage
from module_5_playwright.pages.locators.cart_locators import CHECKOUT_BUTTON_SELECTOR


class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._endpoint = '/cart.html'

    def click_checkout(self) -> None:
        """
        Нажимает на кнопку 'Checkout' на странице корзины.
        """
        self.wait_for_selector_and_click(CHECKOUT_BUTTON_SELECTOR)
