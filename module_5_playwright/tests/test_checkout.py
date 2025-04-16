from playwright.sync_api import Browser, Page
from module_5_playwright.pages.login_page import LoginPage
from module_5_playwright.pages.inventory_page import InventoryPage
from module_5_playwright.pages.cart_page import CartPage
from module_5_playwright.pages.checkout_step_one_page import CheckoutStepOnePage
from module_5_playwright.pages.checkout_step_two_page import CheckoutStepTwoPage
from module_5_playwright.pages.checkout_complete_page import CheckoutCompletePage


def test_add_items_and_checkout(browser: Browser) -> None:
    """
    Тест проверяет полный путь пользователя при оформлении заказа.

    Шаги:
    1. Вход под стандартным пользователем.
    2. Добавление первого товара в корзину.
    3. Переход к оформлению (клик по кнопке Continue).
    4. Заполнение формы оформления заказа.
    5. Подтверждение покупки (клик по кнопке Finish)
    6. Проверка отображение заголовков об успешности оформления заказа и кнопки "Back Home"
    7. Выход из систему через кноку "Logout" в боковом меню

    """
    page: Page = browser.new_page()

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_step_one_page = CheckoutStepOnePage(page)
    checkout_step_two_page = CheckoutStepTwoPage(page)
    checkout_complete_page = CheckoutCompletePage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    cart_page.click_checkout()
    checkout_step_one_page.fill_checkout_form("Kate", "Clap", '12345')
    checkout_step_one_page.click_continue()
    checkout_step_two_page.click_finish()
    checkout_complete_page.checking_order_completion()
    checkout_complete_page.logout()

