import pytest
import requests
from faker import Faker
from module_4.fast_api.constant.constant import HEADERS, BASE_URL


@pytest.fixture()
def auth_session():
    """ Авторизация и получение токена """
    session = requests.Session()
    session.headers.update(HEADERS)
    auth_response = session.post(f"{BASE_URL}/api/v1/login/access-token",data={"username": "test5@mail.ru", "password": "11111111"})
    assert auth_response.status_code == 200
    data_aut = auth_response.json()
    token = auth_response.json().get("access_token")
    assert token is not None, "Токен не найден"
    session.headers.update({"authorization": f"Bearer {token}"})
    return session


@pytest.fixture()
def item(auth_session, item_data):
    """Создание item для дальшейних тестов"""
    response = auth_session.post(f"{BASE_URL}/api/v1/items/", json=item_data)
    assert response.status_code == 200
    item = response.json()
    yield item

    """Удаляем item после каждого теста"""

    delete_response = auth_session.delete(f"{BASE_URL}/api/v1/items/{item['id']}")
    assert delete_response.status_code == 200


@pytest.fixture()
def create_20_items(auth_session):
    """" Создание 20 элементов items """
    for i in range(20):
        data = {
            "title": f"Item {i + 1}",
            "description": f"Description for item {i + 1}"
        }

        create_item_response = auth_session.post(f"{BASE_URL}/api/v1/items/", json=data)
        print(f"[{i + 1}] Status: {create_item_response.status_code}, Response: {create_item_response.json()}")
        assert create_item_response.status_code == 200


fake = Faker()

@pytest.fixture()
def item_data():
    return {
        "title": fake.word().capitalize(),
        "description": fake.sentence(nb_words=10)
    }

fake2 = Faker()

@pytest.fixture()
def put_item_data():
    return {
        "title": fake2.word().capitalize(),
        "description": fake2.sentence(nb_words=10)
    }