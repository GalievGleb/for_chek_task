from for_chek_task.Lupa_pupa.test_playwright.pages.base_page import BasePage
from for_chek_task.Lupa_pupa.test_playwright.locators import BikeLightCardSelectors


class BikeLightPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'inventory-item.html?id=0'

    def add_item_to_cart_and_goto_cart(self):
        """Добавляет товар в корзину и переходит в неё"""
        self.wait_for_selector_and_click(BikeLightCardSelectors.ADD_TO_CARD_SELECTOR)
        self.wait_for_selector_and_click(BikeLightCardSelectors.SHOPPINK_CART_LINK_SELECTOR)
        self.assert_text_present_on_page('Your Cart')