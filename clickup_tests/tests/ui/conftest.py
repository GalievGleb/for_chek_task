import pytest
import allure
from playwright.sync_api import sync_playwright
from faker import Faker

from config.constants import BASE_URL, LIST_ID
from pages.login_page import LoginPage
from utils.helpers import CLICKUP_EMAIL, CLICKUP_PASSWORD

fake = Faker()

@pytest.fixture(scope='session')
def browser():
    with allure.step("Запуск Playwright и открытие браузера"):
        try:
            playwright = sync_playwright().start()
            browser = playwright.chromium.launch(headless=False, slow_mo=1000)
            yield browser
        except Exception as er:
            pytest.fail(f'Ошибка при инициализации браузера: {er}')
        finally:
            with allure.step("Закрытие браузера и Playwright"):
                browser.close()
                playwright.stop()


@pytest.fixture(scope="session")
def login(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    with allure.step("Авторизация на сайте через UI"):
        login_page.login(CLICKUP_EMAIL, CLICKUP_PASSWORD)
    return page


@pytest.fixture
def delete_all_tasks(auth_session):
    def _delete_all_tasks():
        with allure.step("Получаем список всех задач"):
            response = auth_session.get(f"{BASE_URL}/v2/list/{LIST_ID}/task")
            assert response.status_code == 200, f"Ошибка: {response.status_code}, {response.text}"
            tasks = response.json().get('tasks', [])
            assert tasks, 'В ответе нет массива tasks'

        deleted = []
        for task in tasks:
            task_id = task['id']
            with allure.step(f"Удаляем задачу ID={task_id}"):
                resp_del = auth_session.delete(f'{BASE_URL}/v2/task/{task_id}')
                assert resp_del.status_code == 204, f"Ошибка удаления: {resp_del.status_code}, {resp_del.text}"
                deleted.append(task_id)

        with allure.step("Возвращаем список удаленных задач"):
            allure.attach(str(deleted), name="Удаленные задачи", attachment_type=allure.attachment_type.JSON)
        return deleted

    return _delete_all_tasks
