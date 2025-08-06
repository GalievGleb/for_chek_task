import pytest
from for_chek_task.Lupa_pupa.test_playwright.locators import (
    LoginSelectors, InventorySelectors, BikeLightCardSelectors, CheckoutSelectors, MyCartSelectors
                                                              )
from for_chek_task.Lupa_pupa.test_playwright.pages.bike_light_page import BikeLightPage
from for_chek_task.Lupa_pupa.test_playwright.pages.inventory_page import InventoryPage
from for_chek_task.Lupa_pupa.test_playwright.pages.login_page import LoginPage
from for_chek_task.Lupa_pupa.test_playwright.pages.my_cart_page import MyCartPage


def test_add_items_and_checkout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    bike_light_page = BikeLightPage(page)
    my_cart_page = MyCartPage(page)

    login_page.login(LoginSelectors.LOGIN, LoginSelectors.PASSWORD)
    inventory_page.add_backpack_to_cart()
    inventory_page.open_product_bike_light_to_cart()
    bike_light_page.add_item_to_cart_and_goto_cart()
    my_cart_page.check_items_in_cart()
    my_cart_page.start_checkout()
    my_cart_page.fill_checkout_form("Gleb", "Galiev", "1337228")
    my_cart_page.finish_checkout_and_logout()
