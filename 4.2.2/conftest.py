import pytest
import requests
from constant import HEADERS, BASE_URL, auth_data
from faker import Faker

fake = Faker()

@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию с авторизацией и возвращает объект сессии. {"username": "admin", "password": "password123"}"""
    session = requests.Session()
    session.headers.update(HEADERS)

    auth_response = session.post(f"{BASE_URL}/auth", json=auth_data)
    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session

@pytest.fixture()
def booking_data():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Breakfast"
    }

@pytest.fixture()
def upd_booking_data():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-07",
            "checkout": "2024-04-14"
        },
        "additionalneeds": "Breakfast, lunch and dinner"
    }

@pytest.fixture()
def part_updt_booking_data():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name()
    }

@pytest.fixture()
def create_booking(auth_session, booking_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200
        return create_booking.json()

@pytest.fixture()
def empty_booking_data():
    return {
        "firstname": "",
        "lastname": "",
        "totalprice": "",
        "depositpaid": "",
        "bookingdates": {
            "checkin": "",
            "checkout": ""
        },
        "additionalneeds": ""
    }
'''@pytest.fixture()
def delete_booking(auth_session):

    def full_delete(booking_id: int):
        full_delete = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert full_delete.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"'''