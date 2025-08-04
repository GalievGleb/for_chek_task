import pytest
import requests
from faker import Faker

from constant import LOGIN_URL, AUTH_DATA, AUTH_HEADERS, API_HEADERS, ITEM_URL

fake = Faker()


@pytest.fixture()
def item_data():
    """ Генерация случайных данных item
    Return:
        title: Генерация случайного слова
        description: Генерация случайного описания из ~10 слов
    """
    return {
        "title": fake.word().capitalize(),
        "description": fake.sentence(nb_words=10)
    }


@pytest.fixture(scope="session")
def auth_session():
    """ Создаёт и возвращает сессию авторизации

    Args: None

    asserts:
        1.Проверяет статус код, если не 200, то выдаёт статус код и описание ошибки
        2.Проверяет существует ли токен

    Обновление заголовков:
        1.Передается переменная API_HEADERS
        2.Передается токен для авторизации

    return:
        session: сессия для дальнейшего использования
    """
    session = requests.Session()
    response = session.post(url=LOGIN_URL, data=AUTH_DATA, headers=AUTH_HEADERS)
    assert response.status_code == 200, f"Ошибка авторизации: {response.status_code}, {response.json().get('detail')}"

    token = response.json().get("access_token")
    assert token, "Токен отсутствует"

    session.headers.update(API_HEADERS)
    session.headers.update({"Authorization": f"Bearer {token}"})

    return session


@pytest.fixture()
def create_item(auth_session, item_data):
    """ Создаёт item, после всех тестов удаляет его.
    args:
        фикстура item_data
        фикстура auth_session

    asserts:
        1.провеяем статус код, после post запроса
        2.проверка существования item_id
        3.проверяем, равен ли title переданным ранее данным
        4.проверяем статус код, после удаления элемента
        5.проверяем статус код, после post запроса
    """
    response = auth_session.post(ITEM_URL, json=item_data)
    assert response.status_code == 200, f'Ошибка запроса: {response.status_code}, {response.json().get('detail')}'

    data = response.json()
    item_id = data.get("id")
    url_for_tests = ITEM_URL + item_id

    assert item_id is not None
    assert data.get("title") == item_data["title"]

    yield url_for_tests

    response = auth_session.delete(url_for_tests)
    assert response.status_code == 200, f"Элемент с ID: '{item_id}' не удалился"

    response = auth_session.get(url_for_tests)
    assert response.status_code == 404, f"Элемент с ID: '{item_id}' не удалился"





