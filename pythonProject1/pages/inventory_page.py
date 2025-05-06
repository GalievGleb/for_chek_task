import allure
from pages.base_page import BasePage
from  locators.inventory_page_locators import ADD_TO_CARD_SELECTOR, SHOPPING_CARD_LINK_SELECTOR


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'inventory.html'
        self.add_to_card_selector = ADD_TO_CARD_SELECTOR
        self.shopping_card_link_selector = SHOPPING_CARD_LINK_SELECTOR

    @allure.step("Добавление элемента в корзину")
    def add_first_item_to_cart(self):
        """Добавляет первый товар в корзину и переходит в неё.
        Последовательность действий:
        1. Клик по кнопке добавления первого товара в корзину
        2. Проверка видимости иконки корзины
        3. Клик по иконке корзины для перехода к просмотру
        Raises:
            AssertionError: Если иконка корзины не становится видимой
            TimeoutError: Если элементы не найдены в течение заданного времени ожидания
        Note:
            Метод предполагает, что пользователь уже находится на странице с товарами
            """
        self.wait_for_selector_and_click(self.add_to_card_selector)
        self.assert_element_is_visible(self.shopping_card_link_selector)
        self.wait_for_selector_and_click(self.shopping_card_link_selector)
