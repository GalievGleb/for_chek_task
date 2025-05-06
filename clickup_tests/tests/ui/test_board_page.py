import allure
from pages.board_page import BoardPage


@allure.feature("Board UI Tests")
@allure.story("Удаление задач через UI")
@allure.title("Тест удаления задачи на доске")
def test_delete_item(browser, create_task_factory, login):
    """
    Тест на удаление задачи через UI:
    1. Создает задачу через API
    2. Переходит на страницу доски
    3. Открывает созданную задачу
    4. Удаляет задачу через UI
    5. Проверяет, что задача удалена на странице доски
    """
    task_id = create_task_factory()[0]['id']

    board_page = BoardPage(login)
    board_page.go_to_board_page()
    board_page.click_to_task(task_id)
    board_page.delete_task(task_id)
    board_page.check_deleted_task(task_id)


@allure.feature("Board UI Tests")
@allure.story("Создание задач через UI")
@allure.title("Тест создания и удаления задачи на доске")
def test_create_task(login, delete_all_tasks):
    """
    Тест на создание и последующее удаление задачи через UI:
    1. Переходит на страницу доски
    2. Нажимает кнопку создания задачи
    3. Заполняет форму задачи с заданными заголовком и описанием
    4. Удаляет последнюю созданную задачу через API
    5. Проверяет, что удаленная задача больше не отображается на доске
    """
    board_page = BoardPage(login)
    board_page.go_to_board_page()
    board_page.click_create_task_button()
    title = 'Тестовое название'
    description = 'Тестовое описание'
    board_page.fill_task_form(title, description)
    deleted_task = delete_all_tasks()[-1]
    board_page.check_deleted_task(deleted_task)
