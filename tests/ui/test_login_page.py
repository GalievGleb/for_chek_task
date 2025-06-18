from clickup.helpers.utils import CLICKUP_EMAIL, CLICKUP_PASSWORD
from clickup.pages.login_page import LoginPage
import allure

@allure.feature("Тесты авторизации")
class TestLogin:

    @allure.description("Проверка успешного входа в систему")
    @allure.story("Позитивный сценарий авторизации")
    def test_login(browser):
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.login(CLICKUP_EMAIL, CLICKUP_PASSWORD)

    @allure.description("Проверка входа с некорректным паролем")
    @allure.story("Негативный сценарий авторизации")
    def test_failed_login(browser):
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.login(CLICKUP_EMAIL, '12345678')
