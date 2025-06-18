import allure
import pytest
from clickup.api_clients.task_api import ClickUpTaskAPI
from clickup.helpers.utils import CLICKUP_API_KEY, CLICKUP_API
from faker import Faker

fake = Faker()


@pytest.fixture
def task_id_fixture(payload_generated):
    # Фикстура для создания, получения id и названия задачи
    with allure.step("Создание задачи для фикстуры task_id_fixture"):
        name, description = payload_generated
        response = ClickUpTaskAPI.create_task(name, description)
        task_id = response.json()["id"]
        task_name = response.json()["name"]
        return  task_name, task_id


@pytest.fixture
def get_list_fixture(task_api_fixture, get_folder_fixture):
    with allure.step("Получение списка по ID папки"):
        response = task_api_fixture.get_list(get_folder_fixture["id"])
        assert (response.status_code == 200), f"{get_folder_fixture['id']} вернул {response.status_code}"
        list = response.json().get("list")
        assert list, "Список list пуст или отсутствует"
        return list[0]


@pytest.fixture(scope="session")
def task_api_fixture():
    with allure.step("Инициализация TaskAPI и проверка подключения к API"):
        api = ClickUpTaskAPI(CLICKUP_API_KEY, CLICKUP_API)
    with allure.step("Проверка подключения к API через get_task"):
        response = api.get_task()
        assert (response.status_code == 200), f"Ошибка подключения к API {response.status_code} / {response.text}"
    return api


@pytest.fixture
def create_and_delete_task(payload_generated):
    # Фикстура для создания и удаления задачи
    with allure.step("Создание задачи в фикстуре create_and_delete_task"):
        name, description = payload_generated
        create_resp = ClickUpTaskAPI.create_task(name, description)
        assert create_resp.status_code == 200, f"Не удалось создать задачу: {create_resp.text}"
        task_id = create_resp.json().get("id")
        assert task_id, "ID задачи не получен"
        yield create_resp, task_id
    with allure.step(f"Удаление задачи после теста (task_id={task_id})"):
        if task_id:
            ClickUpTaskAPI.delete_task(task_id)


@pytest.fixture()
def payload_generated():
    with allure.step("Генерация данных payload"):
        return fake.word(), fake.word()