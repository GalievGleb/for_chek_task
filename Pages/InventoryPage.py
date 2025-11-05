from Pages.BasePage import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'inventory.html'

    ADD_TO_CART = '#add-to-cart-sauce-labs-backpack'
    BURGER = '#react-burger-menu-btn'
    CREST_BURGER = '#react-burger-cross-btn'
    NAV_1 = '#inventory_sidebar_link'
    NAV_2 = '#about_sidebar_link'
    NAV_3 = '#logout_sidebar_link'
    NAV_4 = '#reset_sidebar_link'
    SHOPPING_CART_LINK = '[data-test="shopping-cart-link"]'

    def check_url(self):
        self.check_to_url()

    def click_to_burger(self):
        self.page.wait_for_selector(self.BURGER)
        self.page.click(self.BURGER)
        self.page.wait_for_selector(self.NAV_1, state='visible')
        self.page.wait_for_selector(self.NAV_2, state='visible')
        self.page.wait_for_selector(self.NAV_3, state='visible')
        self.page.wait_for_selector(self.NAV_4, state='visible')
        self.page.click(self.CREST_BURGER)


    def click_add_to_cart(self):
        self.page.wait_for_selector(self.ADD_TO_CART)
        self.page.click(self.ADD_TO_CART)
        self.wait_for_selector_and_click(self.SHOPPING_CART_LINK)
