import allure
from pages.base_page import BasePage
from locators.finish_page_locators import FINISH_BUTTON_SELECTOR


class FinishPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-two.html'
        self.finish_button_selector = FINISH_BUTTON_SELECTOR

    @allure.step("Переход на следующую страницу checkout")
    def click_finish(self):
        self.wait_for_selector_and_click(self.finish_button_selector)