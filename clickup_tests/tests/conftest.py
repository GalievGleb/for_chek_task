import allure
import pytest
from faker import Faker
from random import randint
from typing import Callable, Any
from requests import Session

from config.constants import HEADERS, BASE_URL, LIST_ID, LIST_NAME
from utils.helpers import CLICKUP_EMAIL, MY_ID, USERNAME, get_initials, check_tag

fake = Faker()

@pytest.fixture(scope='session')
def auth_session() -> Session:
    with allure.step("Создаем авторизованную сессию"):
        session = Session()
        session.headers.update(HEADERS)

        with allure.step("Проверяем аутентификацию пользователя"):
            auth_response = session.get(f"{BASE_URL}/v2/user")
            allure.attach(auth_response.text, name="Ответ при аутентификации", attachment_type=allure.attachment_type.JSON)
            assert auth_response.status_code == 200, f"Ошибка аутентификации: {auth_response.status_code}, {auth_response.text}"
            assert auth_response.json()['user']['email'] == CLICKUP_EMAIL, 'Некорректный email в ответе'

        return session

@pytest.fixture
def generate_create_task_data() -> Callable[[Any], dict[str, str | Any]]:
    def generate(task_id=None):
        with allure.step("Генерируем данные для новой задачи"):
            data = {
                "name": f'task name {fake.word()}',
                "description": fake.sentence(nb_words=10),
                "status": "to do",
                "assignees": [MY_ID],
                "archived": False,
                "tags": [fake.word() for _ in range(5)],
                "priority": randint(1, 4),
                "due_date": 1508299200000,
                "due_date_time": True,
                "time_estimate": 8640000,
                "start_date": 1567569600000,
                "start_date_time": True,
                "parent": task_id,
                "links_to": task_id
            }
            allure.attach(str(data), name="Сгенерированные данные", attachment_type=allure.attachment_type.JSON)
            return data
    return generate

@pytest.fixture
def generate_update_task_data() -> Callable[[Any], dict[str, str | Any]]:
    def generate(task_id=None):
        with allure.step("Генерируем данные для обновления задачи"):
            data = {
                "name": f'task name {fake.word()}',
                "description": fake.sentence(nb_words=10),
                "status": "in progress",
                "assignees": {"add": [MY_ID]},
                "priority": randint(1, 4),
                "due_date": 150549200000,
                "time_estimate": 9040000,
                "start_date": 1597569600000,
                "parent": task_id
            }
            allure.attach(str(data), name="Сгенерированные данные для обновления", attachment_type=allure.attachment_type.JSON)
            return data
    return generate

@pytest.fixture()
def create_task_factory(generate_create_task_data, auth_session):
    created_tasks = []

    def _create_task(data=None):
        if not data:
            data = generate_create_task_data()

        with allure.step("Создаем задачу через API"):
            response = auth_session.post(f"{BASE_URL}/v2/list/{LIST_ID}/task", json=data)
            allure.attach(str(data), name="Тело запроса", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="Ответ сервера", attachment_type=allure.attachment_type.JSON)
            assert response.status_code == 200, f"Ошибка выполнения запроса: {response.status_code}, {response.text}"
            task = response.json()
            created_tasks.append(task.get('id'))
            return task, data

    yield _create_task

    for task_id in created_tasks:
        with allure.step(f"Удаляем задачу {task_id} после теста"):
            delete_task(task_id, auth_session)

def delete_task(task_id, auth_session):
    response = auth_session.delete(f'{BASE_URL}/v2/task/{task_id}')
    allure.attach(f"DELETE /v2/task/{task_id}", name="Удаление задачи", attachment_type=allure.attachment_type.TEXT)
    assert response.status_code == 204, f"Ошибка удаления: {response.status_code}, {response.text}"
