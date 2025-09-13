from faker import Faker
import  pytest
import requests

from module_4.booking.constant.constant import HEADERS, BASE_URL


@pytest.fixture(scope="class")
def auth_session():
        session = requests.Session()
        session.headers.update(HEADERS)
        auth_response = session.post(f"{BASE_URL}/auth", json={"username": "admin", "password" : "password123"})
        assert auth_response.status_code == 200, "Ошибка авторизации"
        token = auth_response.json().get("token")
        assert token is not None, "Токен не найден"
        session.headers.update({"Cookie": f"token={token}"})
        return session

@pytest.fixture(scope="class")
def booking_id(auth_session, booking_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Букинг id не найден"
        return booking_id

fake = Faker()
fake_2 = Faker()
fake_3 = Faker()

@pytest.fixture(scope="class")
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
@pytest.fixture(scope="class")
def booking_data_2():
        return {
                "firstname": fake_2.first_name(),
                "lastname": fake_2.last_name(),
                "totalprice": fake_2.random_int(min=100, max=10000),
                "depositpaid": True,
                "bookingdates": {
                        "checkin": "2024-04-05",
                        "checkout": "2024-04-08"
                },
                "additionalneeds": "Breakfast"
        }
@pytest.fixture(scope="class")
def booking_data_3():
        return {
                "firstname": fake_3.first_name(),
                "lastname": fake_3.last_name()
        }