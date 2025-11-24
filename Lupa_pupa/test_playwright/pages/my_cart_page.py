from for_chek_task.Lupa_pupa.test_playwright.pages.base_page import BasePage
from for_chek_task.Lupa_pupa.test_playwright.locators import MyCartSelectors, CheckoutSelectors


class MyCartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'cart.html'

    def check_items_in_cart(self):
        """Проверяет, отображаются ли в корзине ранее добавленные товары"""
        self.filter_by_text_and_assert_elements_is_visible(
            MyCartSelectors.CART_LIST_SELECTOR, ['Sauce Labs Backpack', 'Sauce Labs Bike Light']
        )
        # self.assert_element_is_visible(MyCartSelectors.FIRST_ITEM_LOCATOR)
        # self.assert_element_is_visible(MyCartSelectors.SECOND_ITEM_LOCATOR)

    def start_checkout(self):
        self.wait_for_selector_and_click(MyCartSelectors.CHECKOUT_LOCATOR)
        self.filter_and_assert_elements_is_visible(CheckoutSelectors.CHECKOUT_INFO_SELECTOR,
                                                   ['[placeholder="First Name"]',
                                                    '[placeholder="Last Name"]',
                                                    '[placeholder="Zip/Postal Code"]'])

    def fill_checkout_form(self, first_name, second_name, postal_code):
        self.wait_for_selector_and_type(CheckoutSelectors.FIRST_NAME_SELECTOR, first_name, 100)
        self.wait_for_selector_and_type(CheckoutSelectors.SECOND_NAME_SELECTOR, second_name, 100)
        self.wait_for_selector_and_type(CheckoutSelectors.ZIP_SELECTOR, postal_code, 100)
        self.assert_input_value(CheckoutSelectors.FIRST_NAME_SELECTOR, first_name)
        self.assert_input_value(CheckoutSelectors.SECOND_NAME_SELECTOR, second_name)
        self.assert_input_value(CheckoutSelectors.ZIP_SELECTOR, postal_code)
        self.wait_for_selector_and_click(CheckoutSelectors.BUTTON_CONTINUE_SELECTOR)
        self.filter_by_text_and_assert_elements_is_visible(
            MyCartSelectors.CART_LIST_SELECTOR, ['Sauce Labs Backpack', 'Sauce Labs Bike Light']
        )

    def finish_checkout_and_logout(self):
        self.wait_for_selector_and_click(CheckoutSelectors.BUTTON_FINISH_SELECTOR)
        self.assert_text_present_on_page('Thank you for your order!')
        self.wait_for_selector_and_click(CheckoutSelectors.BUTTON_OPEN_MENU_SELECTOR)
        self.wait_for_selector_and_click(CheckoutSelectors.BUTTON_LOGOUT_SELECTOR)


