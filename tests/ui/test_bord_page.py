import requests
import allure

from clickup.pages.board_page import BoardPage
from clickup.tests.api.conftest import task_id_fixture
from clickup.tests.constant import BASE_URL, HEADERS
from clickup.tests.ui.conftest import browser


@allure.description("Создание задачи через UI и удаление через API")
@allure.story("Позитивный сценарий создания задачи")
def test_create_task(browser, task_data_generator, login):
    with allure.step("Set up: Инициализация страницы доски"):
        board_page = BoardPage(login)
    with allure.step("Set up: Открытие доски задач"):
        board_page.open_board()
    with allure.step("Test body: Генерация данных задачи"):
        task_data = task_data_generator
        allure.dynamic.title(f"Тест: Создание задачи '{task_data}'")
    with allure.step("Test body: Создание задачи на доске"):
        board_page.create_task(task_data)
    with allure.step("Test body: Получение ID созданной задачи"):
        task_id = board_page.get_task_id(task_data)
        allure.attach(f"Создана задача ID: {task_id}", name="Информация о задаче")
    with allure.step("Tear down: Подготовка к удалению задачи"):
        url = f"{BASE_URL}/v2/task/{task_id}"
    with allure.step("Tear down: Отправка запроса на удаление"):
        response = requests.delete(url, headers=HEADERS)
        allure.attach(f"Статус ответа: {response.status_code}", name="Результат удаления")
    with allure.step("Tear down: Проверка успешности удаления"):
        assert (response.status_code == 204), f"DELETE /task/{task_id} вернул {response.status_code}"


@allure.description("Удаление задачи, созданной через API, через UI")
@allure.story("Позитивный сценарий удаления задачи")
def test_delete_task(browser, task_id_fixture, login):
    with allure.step("Set up: Подготовка тестовых данных"):
        task_data = task_id_fixture[0]
        allure.dynamic.title(f"Тест: Удаление задачи '{task_data}'")
    with allure.step("Set up: Инициализация страницы доски"):
        board_page = BoardPage(login)
    with allure.step("Set up: Открытие доски задач"):
        board_page.open_board()
    with allure.step("Test body: Открытие задачи для удаления"):
        board_page.click_on_task(task_data)
    with allure.step("Test body: Удаление задачи через интерфейс"):
        board_page.delete_task()
    with allure.step("Tear down: Дополнительные проверки после удаления"):
        board_page.check_deleted_task(task_data)
        pass




