from Pages.BasePage import BasePage


class CompletePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-complete.html'


    COMPLETE_TEXT = '.complete-header'
    BUTTON_HOME = '#back-to-products'

    def complete(self):
        self.check_to_url()
        self.wait_for_selector_and_visible(self.COMPLETE_TEXT)
        self.wait_for_selector_and_click(self.BUTTON_HOME)