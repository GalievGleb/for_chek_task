import pytest
import requests
from constant import AUTH_HEADERS, BASE_URL, AUTH_DATA, API_HEADERS
from faker import Faker

fake = Faker()

@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию с авторизацией и возвращает объект сессии. {"username": "t0xa.toxin@yandex.ru", "password": "123456Qwe"}"""
    session = requests.Session()

    response = session.post(f"{BASE_URL}/api/v1/login/access-token", data=AUTH_DATA, headers=AUTH_HEADERS)
    assert response.status_code == 200, f"Auth failed: {response.status_code}, {response.text}"
    token = response.json().get("access_token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update(API_HEADERS)
    session.headers.update({"Authorization": f"Bearer {token}"})

    return session

@pytest.fixture(scope="function")
def item_data():

    return {
            "title": fake.word(),
            "description": fake.sentence(nb_words=10)
        }

@pytest.fixture()
def item_data_20():
    for i in range(20):
        return {
                "title": fake.word(),
                "description": fake.sentence(nb_words=10)
                }