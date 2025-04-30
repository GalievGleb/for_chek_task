from constant import BASE_URL, HEADERS



class TestBookings:

    def test_create_booking(self, booking_data, auth_session, create_booking):
        "Создает бронирование, проверяет данные и статус коды, удаляет бронирование"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        booking_data_response = get_booking.json()
        assert booking_data_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert booking_data_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert booking_data_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert booking_data_response['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert booking_data_response['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"

    def test_updt_booking(self, booking_data, auth_session, upd_booking_data, create_booking):
        "Создает бронирование, обновляет все данные в нём, проверяет обновленные данные и удаляет бронирование"
        booking_id = create_booking.get("bookingid")

        updt_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=upd_booking_data)
        assert updt_booking.status_code == 200

        booking_data_response = updt_booking.json()
        assert booking_data_response['firstname'] == upd_booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == upd_booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert booking_data_response['totalprice'] == upd_booking_data['totalprice'], "Цена не совпадает с заданной"
        assert booking_data_response['depositpaid'] == upd_booking_data['depositpaid'], "Статус депозита не совпадает"
        assert booking_data_response['bookingdates']['checkin'] == upd_booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert booking_data_response['bookingdates']['checkout'] == upd_booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"
        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"


    def test_part_updt_booking(self, booking_data, auth_session, part_updt_booking_data, create_booking):
        "Создает бронирование, частично обновляет(имя и фамилию), проверяет обновленные данные и удаляет бронирование"
        booking_id = create_booking.get("bookingid")

        part_updt_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=part_updt_booking_data)
        assert part_updt_booking.status_code == 200

        booking_data_response = part_updt_booking.json()
        assert booking_data_response['firstname'] == part_updt_booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == part_updt_booking_data['lastname'], "Фамилия не совпадает с заданной"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"
        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"


    def test_get_all_bookings(self, auth_session):
        "Запрашивает id всех бронирований"
        get_all_bookings = auth_session.get(f"{BASE_URL}/booking")
        assert get_all_bookings.status_code == 200
        print(get_all_bookings.json())

    def test_empty_booking(self, auth_session,empty_booking_data):
        "Создает бронирование не заполняя ни одного поля"
        create_empty_booking = auth_session.post(f"{BASE_URL}/booking", json=empty_booking_data)
        assert create_empty_booking.status_code == 200
        booking_id = create_empty_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"
        print(create_empty_booking.json())

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"
        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"

    def test_wrong_type_booking(self, auth_session):
        "Создает бронирование заполняя поля неверными типами данных"
        create_wrong_booking = auth_session.post(f"{BASE_URL}/booking", json={
        "firstname": 1234,
        "lastname": 1234,
        "totalprice": "Alex",
        "depositpaid": 1234,
        "bookingdates": {
            "checkin": "2024-20-20",
            "checkout": "2024-13-14"
        },
        "additionalneeds": ""
    })
        assert create_wrong_booking.status_code == 500, "Бронирование создано"

