from playwright.sync_api import expect, Page, Locator
from typing import Union

class BasePage:
    __BASE_URL = 'https://www.saucedemo.com'

    def __init__(self, page: Page):
        self.page: Page = page
        self._endpoint: str = ''

    def _get_full_url(self) -> str:
        return f'{self.__BASE_URL}/{self._endpoint}'

    def navigate_to(self) -> None:
        full_url = self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(full_url)

    def wait_for_selector_and_click(self, selector: str) -> None:
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def wait_for_selector_and_fill(self, selector: str, value: str) -> None:
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)

    # прочитала, что type нужен для иммитации ручного ввода и такой метод больше подходит ситуациям,
    # где пользователь вводит слово по буквам и под полем появляется  выпадающий список автоподсказок
    # на нашем сайте такого нет, поэтому везде использовала fill

    # def wait_for_selector_and_type(self, selector, value, delay):
    #     self.page.wait_for_selector(selector)
    #     self.page.type(selector, value, delay=delay)

    def assert_element_is_visible(self, selector: str) -> None:
        expect(self.page.locator(selector)).to_be_visible()

    def assert_text_present_on_page(self, text: str) -> None:
        expect(self.page.locator('body')).to_contain_text(text)

    def assert_text_in_element(self, selector: str, text: str) -> None:
        expect(self.page.locator(selector)).to_have_text(text)

# не совсем поняла, зачем нужна эта проверка. Зачем проверять, что пост-код равнен 1234, если на предыдущем шаге это
# вводится автоматически. Разве может ввестись что-то иное?
#     def assert_input_value(self, selector, expected_value):
#         expect(self.page.locator(selector)).to_have_text(expected_value)
