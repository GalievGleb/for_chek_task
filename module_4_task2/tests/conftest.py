import pytest
import requests
from module_4_task2.config.const import AUTH_HEADERS, BASE_URL, AUTH_DATA, API_HEADERS
from faker import Faker
fake1 = Faker()
fake = Faker()

@pytest.fixture(scope="session")
def auth_session():

    # Аутентификация
    session = requests.Session()
    response = session.post(f"{BASE_URL}/api/v1/login/access-token", data=AUTH_DATA, headers=AUTH_HEADERS)
    assert response.status_code == 200, f"Ошибка аутентификации: {response.status_code}, {response.text}"
    # Получение токена
    token = response.json().get("access_token")
    assert token, "Токен не найден"

    # Настройка заголовков сессии
    session.headers.update(API_HEADERS)
    session.headers.update({"Authorization": f"Bearer {token}"})

    return session


@pytest.fixture()
def item_data():
    """
        Фикстура для генерации тестовых данных элемента.

        Returns:
            function: Функция, возвращающая словарь с тестовыми данными
        """
    return {
        "title": fake.word().capitalize(),
        "description": fake.sentence(nb_words=10)
    }


@pytest.fixture()
def update_item():
    return {
        "title": fake1.word().capitalize(),
        "description": fake1.sentence(nb_words=10)
    }

@pytest.fixture(scope='function')
def auth_session_without_token():
    """Фикстура для создания неавторизованной сессии (без токена).

        Returns:
            Session: HTTP-сессия без авторизационных заголовков
        """
    session = requests.Session()
    session.headers.update(API_HEADERS)
    return session


def creat ():
    session = requests.Session()
    for i in range(20):
        data = {
        "title": fake1.word().capitalize(),
        "description": fake1.sentence(nb_words=10)
    }
        creat_items = session.post(f'{BASE_URL}/api/v1/items/', json = data)
        assert creat_items.status_code == 200, 'Не создалось 20 итемов'