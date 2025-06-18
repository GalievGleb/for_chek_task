from playwright.sync_api import expect
import allure



class BasePage:
    _BASE_URL = 'https://app.clickup.com'

    def __init__(self, page):
        self.page = page
        self._endpoint = ""

    def _get_full_url(self):
        return f'{self._BASE_URL}/{self._endpoint}'

    @allure.step("Навигация по странице")
    def navigate_to(self):
        full_url = self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(full_url)

    @allure.step("Клик по селектору: {selector}")
    def wait_for_selector_and_click(self, selector):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    @allure.step("Передача текста в {selector}")
    def wait_for_selector_and_fill(self, selector, value):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)

    @allure.step("Ввод текста с задержкой в {selector}")
    def wait_for_selector_and_type(self, selector, value, delay):
        self.page.wait_for_selector(selector)
        self.page.type(selector, value, delay=delay)

    @allure.step("Проверка видимости селектора - {selector} ")
    def assert_element_is_visible(self, selector):
        expect(self.page.locator(selector)).to_be_visible()

    @allure.step("Проверка наличия {expected_value} в body")
    def assert_text_is_on_page(self, expected_value, timeout):
        expect(self.page.locator("body")).to_contain_text(expected_value, timeout=timeout)

    @allure.step("Проверка наличия {input_value} в {selector}")
    def assert_input_value(self, selector, input_value):
        expect(self.page.locator(selector)).to_have_value(input_value)

    @allure.step("Проверка отсутствия селектора - {selector} ")
    def assert_element_is_not_visible(self, selector):
        expect(self.page.locator(selector)).not_to_be_visible()