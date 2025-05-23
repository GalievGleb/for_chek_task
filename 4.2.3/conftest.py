from tokenize import endpats

import pytest
import requests
from typing_extensions import final

from constant import AUTH_HEADERS, BASE_URL, AUTH_DATA, API_HEADERS, endpoint
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


@pytest.fixture()
def delete_all_items_before_test_and_after(auth_session):
    get_response = auth_session.get(endpoint)
    assert get_response.status_code == 200, (
        f"Ошибка получения списка элементов: {get_response.text}"
    )

    for item in get_response.json().get('data', []):
        item_id = item['id']
        del_response = auth_session.delete(f"{endpoint}{item_id}")
        assert del_response.status_code in (200, 204), (
            f"Ошибка удаления элементов: {get_response.text}")

    final_check = auth_session.get(endpoint)
    assert len(final_check.json().get("data",[])) == 0, (
        "не все элементы были удалены перед тестом")