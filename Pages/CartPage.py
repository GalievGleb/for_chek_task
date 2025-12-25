from Pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'cart.html'

    ITEM_CART = '.cart_item'
    ITEM_NAME = '.inventory_item_name'
    SHOPPING_CART_LINK = '[data-test="shopping-cart-link"]'
    BUTTON_CHECKOUT = '#checkout'

    def check_url(self):
        self.check_to_url()


    def wait_for_selector(self):
        self.wait_for_selector_enabled(self.ITEM_CART)
        self.wait_for_selector_and_click(self.ITEM_NAME)
        self.wait_for_selector_and_click(self.SHOPPING_CART_LINK)
        self.wait_for_selector_and_click(self.BUTTON_CHECKOUT)


