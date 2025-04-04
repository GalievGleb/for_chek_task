import pytest
import requests
from constant import BASE_URL, AUTH_HEADERS, HEADERS
from faker import Faker


@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию с авторизацией и возвращает объект сессии."""
    session = requests.Session()
    session.headers.update(AUTH_HEADERS)

    # Данные для получения токена
    data = {
        "grant_type": "password",
        "username": "katebb0310@gmail.com",
        "password": "qwerty123",
        "scope": "",
        "client_id": "string",
        "client_secret": "string"
    }

    auth_response = session.post(f"{BASE_URL}/api/v1/login/access-token", data=data, headers=AUTH_HEADERS)
    assert auth_response.status_code == 200, f"Ошибка авторизации, статус код: {auth_response.status_code}"
    print(f"Authorization response: {auth_response.status_code}, {auth_response.text}")
    token = auth_response.json().get("access_token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Authorization": f"Bearer {token}"})
    session.headers.update({"Content-Type": "application/json"})
    return session

@pytest.fixture
def random_item_data():
    fake = Faker()
    return {
        "title": fake.word(),
        "description": fake.sentence()
    }




