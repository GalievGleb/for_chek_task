import requests
import pytest
from faker import Faker
from constant import USERNAME, PASSWORD, HEADERS, BASE_URL

faker = Faker()
@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию с авторизацией и возвращает объект сессии."""
    session = requests.Session()
    session.headers.update(HEADERS)

    # Используем USERNAME и PASSWORD из constants
    auth_response = session.post(f"{BASE_URL}/auth", headers=HEADERS, json={"username": USERNAME, "password": PASSWORD})
    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session

@pytest.fixture()
def booking_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Breakfast"
    }

@pytest.fixture
def create_booking(auth_session, booking_data):
    """Фикстура для создания бронирования и возвращения его ID и данных."""
    create_response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    assert create_response.status_code == 200, "Ошибка при создании букинга"
    booking_id = create_response.json().get("bookingid")
    assert booking_id is not None, "ID букинга не найден в ответе"
    return booking_id, create_response.json()

@pytest.fixture
def delete_booking(auth_session):
    """Фикстура для удаления бронирования с использованием yield."""

    def _delete_booking(booking_id):
        delete_response = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_response.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"
        check_delete_response = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert check_delete_response.status_code == 404, f"Букинг с ID {booking_id} не был удален"

    yield _delete_booking