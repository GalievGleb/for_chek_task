from clickup.pages.base_page import BasePage
from clickup.helpers.utils import TEAM_ID
import allure

@allure.feature("Функционал Доски")
class BoardPage(BasePage):

    CREATE_BUTTON = '[data-test="board-group-header__create-task-button__to do"]'
    DELETE_BUTTON = '[data-test="quick-actions-menu__delete-task"]'
    TASK_INPUT = '[data-test="quick-create-task-panel__panel-board__input"]'
    SAVE_BUTTON = '[data-test="quick-create-task-panel__panel-board__enter-button"]'
    UNDO_DELETE = '[data-test="undo-toast-items__toast-undo"]'
    Board_Action = '[data-test="board-actions-menu__ellipsis__{task_data}"]'
    TASK_BUTTON = '[data-test="board-task__name-link__{task_data}"]'
    ELLIPSIS = '[data-test="task-view-header__task-settings"]'
    DROPDOWN_DELETE = '[data-test="dropdown-list-item__Delete"]'
    GET_ID_SELECTOR = '[data-test="cu-task-view-task-label__task-id"]'
    BOARD_BUTTON = '[data-test="data-view-item__view-id-body-Board"]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = f'{TEAM_ID}/v/b/t/{TEAM_ID}'
        if page is None:
            raise ValueError("Page object cannot be None")
        self.page = page


    @allure.step("Открываем доску")
    def open_board(self):
        with allure.step("Ожидание загрузки страницы"):
            self.page.wait_for_load_state("load")
        with allure.step("Клик по кнопке доски"):
            self.wait_for_selector_and_click(self.BOARD_BUTTON)


    @allure.step("Создание задачи: '{task_data}'")
    def create_task(self, task_data):
        with allure.step("Навигация на страницу доски"):
            self.navigate_to()
        with allure.step("Клик по кнопке создания задачи"):
            self.wait_for_selector_and_click(self.CREATE_BUTTON)
        with allure.step(f"Ввод данных задачи: '{task_data}'"):
            self.wait_for_selector_and_type(self.TASK_INPUT, task_data, delay=300)
        with allure.step("Сохранение задачи"):
            self.wait_for_selector_and_click(self.SAVE_BUTTON)


    @allure.step("Удаление задачи через доску")
    def board_delete_task(self):
        with allure.step("Навигация на страницу доски"):
            self.navigate_to()
        with allure.step("Клик по кнопке удаления"):
            self.wait_for_selector_and_click(self.DELETE_BUTTON)
        with allure.step("Проверка видимости кнопки отмены удаления"):
            self.assert_element_is_visible(self.UNDO_DELETE)


    @allure.step("Удаление задачи через меню")
    def delete_task(self):
        with allure.step("Открытие меню задачи"):
            self.wait_for_selector_and_click(self.ELLIPSIS)
        with allure.step("Выбор пункта 'Удалить'"):
            self.wait_for_selector_and_click(self.DROPDOWN_DELETE)


    @allure.step("Клик по задаче: '{task_data}'")
    def click_on_task(self, task_data):
        selector = self.TASK_BUTTON.format(task_data=task_data)
        with allure.step(f"Проверка видимости задачи: '{task_data}'"):
            self.assert_element_is_visible(selector)
        with allure.step(f"Клик по задаче: '{task_data}'"):
            self.wait_for_selector_and_click(selector)


    @allure.step("Получение ID задачи: '{task_data}'")
    def get_task_id(self, task_data):
        with allure.step("Открытие задачи"):
            self.click_on_task(task_data)
        with allure.step("Проверка видимости элемента с ID"):
            self.assert_element_is_visible(self.GET_ID_SELECTOR)
        with allure.step("Извлечение текста из элемента"):
            button = self.page.query_selector(self.GET_ID_SELECTOR)
            button_text = button.text_content()
        with allure.step("Обработка текста для получения ID"):
            task_id = button_text.replace('Copy Task ID', '').strip()
            allure.attach(f"Полученный ID задачи: {task_id}", name="Task ID")
        return task_id


    @allure.step("Проверить, что задача удалена: {task_id}")
    def check_deleted_task(self, task_id):
        self.assert_element_is_not_visible(f'[data-id="{task_id}"]')