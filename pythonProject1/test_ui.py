import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.finish_page import FinishPage
from pages.logout_page import LogoutPage
from constant import user_name, password, first_name, last_name, postal_code


@allure.title("Полный путь проверки")
@allure.feature("Оформление заказа")
@allure.story("Пользователь может добавить товар и завершить оформление заказа")
def test_add_items_and_checkout(browser):
    """
    E2E тест полного цикла покупки: от авторизации до выхода из системы.
    Шаги теста:
    1. Авторизация стандартного пользователя
    2. Добавление первого товара в корзину
    3. Начало оформления заказа
    4. Заполнение данных для доставки
    5. Завершение оформления заказа
    6. Проверка страницы завершения
    7. Выход из системы

    Ожидаемый результат:
    Все шаги выполняются без ошибок, пользователь может завершить полный цикл покупки.
    """
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    finish_page = FinishPage(page)
    logout_page = LogoutPage(page)

    login_page.login(user_name, password)
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form(first_name, last_name, postal_code)
    checkout_page.click_continue()
    finish_page.click_finish()
    logout_page.check_logout_page()
    logout_page.logout()
