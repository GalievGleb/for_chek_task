from Pages.BasePage import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-one.html'

    INPUT_FIRST_NAME = '#first-name'
    INPUT_LAST_NAME = '#last-name'
    INPUT_POSTAL_CODE = '#postal-code'
    BUTTON_CONTINUE = '#continue'
    BUTTON_FINISH = '#finish'



    def fill_in_details(self, first_name, last_name, postal_code):
        self.check_to_url()
        self.wait_for_selector_and_fill(self.INPUT_FIRST_NAME, first_name)
        self.wait_for_selector_and_fill(self. INPUT_LAST_NAME, last_name)
        self.wait_for_selector_and_fill(self.INPUT_POSTAL_CODE, postal_code)
        self.wait_for_selector_and_click(self.BUTTON_CONTINUE)
        self.wait_for_selector_and_click(self.BUTTON_FINISH)
