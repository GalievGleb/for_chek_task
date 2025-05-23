from for_chek_task.five.pages.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_BUTTON_SELECTOR = '[id="checkout"]'
    FIRST_NAME_SELECTOR = '#first-name'
    LAST_NAME_SELECTOR = '#last-name'
    POSTAL_CODE_SELECTOR = 'input[name="postalCode"]'
    CONTINUE_BUTTON = '[id="continue"]'
    FINNISH_BUTTON = '[id="finish"]'
    BURGER_BUTTON = '[id="react-burger-menu-btn"]'
    LOGOFF_BUTTON = '[id="logout_sidebar_link"]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-one.html'

    def start_checkout(self):
        self.wait_for_selector_and_click(self.CHECKOUT_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.FIRST_NAME_SELECTOR)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.wait_for_selector_and_type(self.FIRST_NAME_SELECTOR, first_name, 100)
        self.wait_for_selector_and_type(self.LAST_NAME_SELECTOR, last_name, 100)
        self.wait_for_selector_and_type(self.POSTAL_CODE_SELECTOR, postal_code, 100)
        self.assert_input_value(self.POSTAL_CODE_SELECTOR, postal_code)

    def continue_checkout(self):
        self.wait_for_selector_and_click(self.CONTINUE_BUTTON)
        self.assert_element_is_visible(self.FINNISH_BUTTON)
        self.wait_for_selector_and_click(self.FINNISH_BUTTON)

    def start_logout(self):
        self.wait_for_selector_and_click(self.BURGER_BUTTON)
        self.assert_element_is_visible(self.LOGOFF_BUTTON)
        self.wait_for_selector_and_click(self.LOGOFF_BUTTON)