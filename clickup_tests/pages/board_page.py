from locators.board_page_locators import ADD_TASK_BUTTON_SELECTOR, TASK_TITLE_SELECTOR, DESCRIPTION_SELECTOR, \
    DESCRIPTION_BUTTON_SELECTOR, PRIORITY_BUTTON_SELECTOR, PRIORITY_SELECTOR, CREATE_TASK_BUTTON_SELECTOR, \
    CHECK_TASK_SELECTOR, BOARD_SELECTOR
from pages.base_page import BasePage
from utils.helpers import TEAM_ID, BOARD_ID
import allure


class BoardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = f'{TEAM_ID}/v/o/s/{BOARD_ID}'

    @allure.step("Нажать кнопку создания задачи")
    def click_create_task_button(self):
        self.assert_element_is_visible(ADD_TASK_BUTTON_SELECTOR)
        self.wait_for_selector_and_click(ADD_TASK_BUTTON_SELECTOR)
        self.assert_element_is_visible(TASK_TITLE_SELECTOR)

    @allure.step("Заполнить форму задачи: {title}, {description}")
    def fill_task_form(self, title, description):
        with allure.step("Ввод заголовка задачи"):
            self.wait_for_selector_and_fill(TASK_TITLE_SELECTOR, title)
        with allure.step("Открыть поле описания"):
            self.wait_for_selector_and_click(DESCRIPTION_BUTTON_SELECTOR)
        with allure.step("Ввод описания задачи"):
            self.wait_for_selector_and_fill(DESCRIPTION_SELECTOR, description)
        with allure.step("Выставить приоритет задачи"):
            self.wait_for_selector_and_click(PRIORITY_BUTTON_SELECTOR)
            self.wait_for_selector_and_click(PRIORITY_SELECTOR)
        with allure.step("Нажать кнопку 'Создать'"):
            self.wait_for_selector_and_click(CREATE_TASK_BUTTON_SELECTOR)
        with allure.step("Проверить, что задача появилась на доске"):
            self.assert_text_in_element(CHECK_TASK_SELECTOR, title)

    @allure.step("Перейти на страницу доски")
    def go_to_board_page(self):
        with allure.step("Открыть URL доски"):
            self.navigate_to()
        with allure.step("Перейти в раздел 'Board'"):
            self.wait_for_selector_and_click(BOARD_SELECTOR)

    @allure.step("Клик по задаче с ID: {task_id}")
    def click_to_task(self, task_id):
        self.wait_for_selector_and_click(f'[data-id="{task_id}"] [type="button"]')

    @allure.step("Удалить задачу с ID: {task_id}")
    def delete_task(self, task_id):
        with allure.step("Открыть настройки задачи"):
            self.wait_for_selector_and_click('[data-test="task-view-header__task-settings"]')
        with allure.step("Выбрать 'Удалить'"):
            self.wait_for_selector_and_click('[data-test="dropdown-list-item__cu-task-view-menu-delete"]')

    @allure.step("Проверить, что задача удалена: {task_id}")
    def check_deleted_task(self, task_id):
        self.assert_element_is_not_visible(f'[data-id="{task_id}"]')
