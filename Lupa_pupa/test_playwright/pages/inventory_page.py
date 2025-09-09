from for_chek_task.Lupa_pupa.test_playwright.pages.base_page import BasePage
from for_chek_task.Lupa_pupa.test_playwright.locators import InventorySelectors


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'inventory.html'

    def add_backpack_to_cart(self):
        """Добавление товара Backpack в корзину"""
        self.wait_for_selector_and_click(InventorySelectors.ADD_TO_BackPack_CARD_SELECTOR)

    def open_product_bike_light_to_cart(self):
        """Открывает товар Bike Light"""
        self.wait_for_selector_and_click(InventorySelectors.PRODUCT_BikeLight_CARD_SELECTOR)
        self.assert_text_present_on_page('Back to products')