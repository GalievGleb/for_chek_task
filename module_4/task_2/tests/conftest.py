import pytest
import requests
from typing import Dict, Callable, Generator
from requests import Session
from module_4.task_2.config.constant import BASE_URL, AUTH_HEADERS, HEADERS, AUTH_DATA
from faker import Faker
import logging

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

faker = Faker()

@pytest.fixture(scope="session")
def auth_session() -> Session:
    """Создаёт сессию с авторизацией и возвращает объект сессии."""
    session = requests.Session()
    session.headers.update(AUTH_HEADERS)

    # Данные для получения токена
    data = AUTH_DATA

    auth_response = session.post(f"{BASE_URL}/api/v1/login/access-token", data=data, headers=AUTH_HEADERS)
    assert auth_response.status_code == 200, f"Ошибка авторизации, статус код: {auth_response.status_code}"
    print(f"Authorization response: {auth_response.status_code}, {auth_response.text}")
    token = auth_response.json().get("access_token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Authorization": f"Bearer {token}"})
    session.headers.update({"Content-Type": "application/json"})
    return session

@pytest.fixture
def random_item_data() -> Dict[str, str]:
    """Генерация случайных данных для item"""
    return {
        "title": faker.word(),
        "description": faker.sentence(),
    }

@pytest.fixture
def create_item() -> Callable[[Session, Dict[str, str]], Dict[str, str]]:
    """Фикстура для создания нового item"""
    def _create_item(auth_session: Session, random_item_data: Dict[str, str]) -> Dict[str, str]:
        create_response = auth_session.post(f"{BASE_URL}/api/v1/items/", json=random_item_data, headers=HEADERS)
        assert create_response.status_code == 200, "Ошибка при создании item"

        created_item = create_response.json()
        assert "id" in created_item, "ID item не найден"
        assert created_item["title"] == random_item_data["title"], "Название не совпадает"
        assert created_item["description"] == random_item_data["description"], "Описание не совпадает"

        return created_item  # Возвращаем созданный элемент с ID
    return _create_item

@pytest.fixture
def delete_item() -> Callable[[Session, int], None]:
    """Фикстура для удаления item по ID"""
    def _delete_item(auth_session: Session, item_id: int) -> None:
        delete_response = auth_session.delete(f"{BASE_URL}/api/v1/items/{item_id}", headers=HEADERS)
        assert delete_response.status_code == 200, f"Ошибка при удалении item с ID {item_id}"

        # Проверяем, что item был удален
        check_delete_response = auth_session.get(f"{BASE_URL}/api/v1/items/{item_id}", headers=HEADERS)
        assert check_delete_response.status_code == 404, f"Item с ID {item_id} не был удален"
    return _delete_item
