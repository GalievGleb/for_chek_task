import allure
from pages.base_page import BasePage
from locators.checkout_page_locators import (CHECKOUT_BUTTON_SELECTOR, FIRST_NAME_SELECTOR, LAST_NAME_SELECTOR,
                                             POSTAL_CODE_SELECTOR, CONTINUE_BUTTON_SELECTOR)


class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-one.html'
        self.checkout_button_selector = CHECKOUT_BUTTON_SELECTOR
        self.first_name_selector = FIRST_NAME_SELECTOR
        self.last_name_selector = LAST_NAME_SELECTOR
        self.postal_selector = POSTAL_CODE_SELECTOR
        self.continue_button_selector = CONTINUE_BUTTON_SELECTOR

    @allure.step("Переход на страницу checkout")
    def start_checkout(self):
        """
        Переходит на страницу оформления заказа (checkout).
        Действия:
        1. Ожидает появления и кликает на кнопку перехода к оформлению заказа.
        2. Проверяет видимость поля для ввода имени (убеждается, что страница загрузилась).
        """
        self.wait_for_selector_and_click(self.checkout_button_selector)
        self.assert_element_is_visible(self.first_name_selector)

    @allure.step("Заполнение формы checkout")
    def fill_checkout_form(self, first_name, last_name, postal_code):
        """
        Заполняет форму оформления заказа указанными данными.
        Параметры:
            first_name (str): Имя покупателя
            last_name (str): Фамилия покупателя
            postal_code (str): Почтовый индекс
        Действия:
        1. Заполняет поля имени, фамилии и почтового индекса.
        2. Проверяет, что значение почтового индекса было корректно установлено.
        """
        self.wait_for_selector_and_type(self.first_name_selector, first_name)
        self.wait_for_selector_and_type(self.last_name_selector, last_name)
        self.wait_for_selector_and_type(self.postal_selector, postal_code)
        self.assert_input_value(self.postal_selector, postal_code)

    @allure.step("Нажатие на кнопку для перехода на след. страницу")
    def click_continue(self):
        """
        Нажимает кнопку продолжения оформления заказа.
        Действия:
        1. Ожидает появления и кликает на кнопку продолжения.
        """
        self.wait_for_selector_and_click(self.continue_button_selector)