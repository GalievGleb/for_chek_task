from Pages.CartPage import CartPage
from Pages.CheckoutPage import CheckoutPage
from Pages.CompletePage import CompletePage
from Pages.InventoryPage import InventoryPage
from Pages.LoginPage import LoginPage


def test_start(browser):
    page = browser.new_page()
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    complete = CompletePage(page)

    login.login('standard_user', 'secret_sauce')
    inventory.check_url()
    inventory.click_to_burger()
    inventory.click_add_to_cart()
    cart.check_url()
    cart.wait_for_selector()
    checkout.fill_in_details('John', 'Snow', '123455')
    complete.complete()


