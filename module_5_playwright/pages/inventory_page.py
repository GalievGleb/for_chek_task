from module_5_playwright.pages.base_page import BasePage
from playwright.sync_api import Page
from module_5_playwright.pages.locators.inventory_locators import *


class InventoryPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._endpoint = '/inventory.html'

    def add_first_item_to_cart(self) -> None:
        """
        Добавляет первый товар в корзину и переходит на страницу корзины через клик на иконку "Cart".
        """
        self.wait_for_selector_and_click(ADD_TO_CARD_SELECTOR)
        self.assert_element_is_visible(SHOPPING_CART_LINK_SELECTOR)
        self.wait_for_selector_and_click(SHOPPING_CART_LINK_SELECTOR)

