from http.client import responses
from http.cookiejar import Cookie
from const import HEADERS , BASE_URL, json_auth
import requests
import pytest
from requests import session


class TestBooking:

    def test_creat(self, auth, booking_data):

        creat_book=auth.post(f'{BASE_URL}/booking', json=booking_data)
        assert creat_book.status_code == 200, 'Ошибка при создании брони'
        id=creat_book.json().get("bookingid")
        assert id is not None, 'Айди нет в ответе'
        assert creat_book.json()["booking"]["firstname"]==booking_data["firstname"], 'Имя не  совпадает'

        get_booking = auth.get(f"{BASE_URL}/booking/{id}")
        assert get_booking.status_code == 200

        get_booking_noid=auth.get(f'{BASE_URL}/booking')
        assert get_booking_noid.status_code == 200, 'Нет данных о брони'

    def test_put(self,auth,created_booking):
        booking_id=created_booking

        data_put= {
        "firstname" : "James",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
             "checkin" : "2018-01-01",
             "checkout" : "2019-01-01"
         },
        "additionalneeds" : "Breakfast"
         }

        put_book=auth.put(f'{BASE_URL}/booking/{booking_id}', json=data_put)
        assert put_book.status_code == 200 , 'Ошибка при обновлении'

        get_response=auth.get(f'{BASE_URL}/booking/{booking_id}')
        assert get_response.status_code == 200
        assert get_response.json()["firstname"] == "James"