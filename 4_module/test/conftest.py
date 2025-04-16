from http.client import responses
from http.cookiejar import Cookie

import pytest
import requests


from const import HEADERS , BASE_URL, json_auth
from faker import Faker
faker = Faker()


@pytest.fixture(scope="session")
def auth():
    session=requests.Session()
    session.headers.update(HEADERS)

    response=requests.post(f"{BASE_URL}/auth",headers=HEADERS, json=json_auth)
    assert response.status_code == 200, "Ошибка авторизации"
    token = response.json().get('token')
    assert token is not None, 'Нет токена'

    session.headers.update({"Cookie":f"token={token}"})
    return session


@pytest.fixture()
def booking_data():
    return {
        "firstname" : faker.first_name(),
        "lastname" : faker.last_name(),
        "totalprice" : faker.random_int(min=110, max= 100000),
        "depositpaid" : True,
        "bookingdates" : {
             "checkin" : "2018-01-01",
             "checkout" : "2019-01-01"
         },
        "additionalneeds" : "Breakfast"
         }
@pytest.fixture()
def created_booking(auth, booking_data):
    response = auth.post(f"{BASE_URL}/booking", json=booking_data)
    assert response.status_code == 200, "Ошибка при создании брони"
    booking_id = response.json()["bookingid"]
    assert booking_id is not None, 'Нет Айди'
    return booking_id

