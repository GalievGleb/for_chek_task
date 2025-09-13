from playwright.sync_api import expect
from typing import List


class BasePage:
    """Базовый URL с использованием инкапсуляции"""
    __BASE_URL = "https://www.saucedemo.com/"

    def __init__(self, page):
        self.page = page
        self._endpoint = ''

    def _get_full_url(self) -> str:
        """Получает полный URL
        return:
            Полный URL(BASE_URL+ENDPOINT)
        """
        return f"{self.__BASE_URL}{self._endpoint}"

    def navigate_to(self):
        """Открывает браузер с нужным URL"""
        full_url = self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_url(full_url)

    def wait_for_selector_and_click(self, selector):
        """Ждёт пока появится нужный элемент и кликает на него
        args:
            selector: элемент для взаимодействия с ним
        """
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def wait_for_selector_and_fill(self, selector, value):
        """Ждёт пока появится нужный элемент и вводит в нём нужный текст(ctrl+v)
        args:
            selector: элемент для взаимодействия с ним
            value: используемый текст
        """
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)

    def wait_for_selector_and_type(self, selector, value, delay):
        """Ждёт пока появится нужный элемент и вводит текст имитируя поочередное нажатие на клавиши
        args:
            selector: элемент для взаимодействия с ним
            value: используемый текст
            delay: скорость ввода текста
        """
        self.page.wait_for_selector(selector)
        self.page.type(selector, value, delay=delay)

    def filter_by_text_and_assert_elements_is_visible(self, selector: str, texts: List[str]):
        """Решил от себя добавить такой метод
        Ищет по тексту локарторы в родительском элементе и проверяет видимость каждого элемента
        из списка на странице.

        args:
            selector: Родительский селектор для поиска в нём локаторов с помощью метода filter
            texts: Передается список текста для поиска
        """
        for text in texts:
            expect(self.page.locator(selector).filter(has_text=text)).to_be_visible()

    def filter_and_assert_elements_is_visible(self, selector: str, elements: List[str]):
        """Решил от себя добавить такой метод
        Ищет дочерие элементы в родительском элементе и проверяет их видимость на странице.

        args:
            selector: Родительский селектор для поиска в нём локаторов с помощью метода filter
            moretext: Передается список текста для поиска
        """
        for element in elements:
            expect(self.page.locator(selector).filter(has=self.page.locator(element))).to_be_visible()

    def assert_element_is_visible(self, selector):
        """Проверяет видимосость элемента на странице
        args:
            selector: элемент для взаимодействия с ним
        """
        expect(self.page.locator(selector)).to_be_visible()

    def assert_text_present_on_page(self, text):
        """Проверяет содержимость текста на странице
        args:
            text: текст для проверки
        """
        expect(self.page.locator("body")).to_contain_text(text)

    def assert_text_in_element(self, selector, text):
        """Проверяет содержимость текста внутри элемента
        args:
            selector: элемент для взаимодействия с ним
            text: текст для проверки
        """
        expect(self.page.locator(selector)).to_have_text(text)

    def assert_input_value(self, selector, expected_value):
        """Проверяет вводимое значение
        args:
            selector: элемент для взаимодействия с ним
            expected_value: текст для проверки
        """
        expect(self.page.locator(selector)).to_have_value(expected_value)