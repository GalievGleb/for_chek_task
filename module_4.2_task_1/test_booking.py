from faker import Faker
from constant import BASE_URL, HEADERS
import requests

faker = Faker()

class TestBooking:

    def create_booking(self, auth_session, booking_data):
        create_response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_response.status_code == 200, "Ошибка при создании букинга"
        booking_id = create_response.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"
        return booking_id, create_response.json()

    def delete_booking(self, auth_session, booking_id):
        delete_response = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_response.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"
        check_delete_response = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert check_delete_response.status_code == 404, f"Букинг с ID {booking_id} не был удален"

# positive checks
    def test_create_booking(self, auth_session, booking_data):
        booking_id, create_response = self.create_booking(auth_session, booking_data)

        # Проверка созданного бронирования
        assert create_response["booking"]["firstname"] == booking_data["firstname"]
        assert create_response["booking"]["lastname"] == booking_data["lastname"]
        assert create_response["booking"]["totalprice"] == booking_data["totalprice"]
        assert create_response["booking"]["additionalneeds"] == booking_data["additionalneeds"]

        # Удаляем бронирование
        self.delete_booking(auth_session, booking_id)

    def test_full_update_booking(self, auth_session, booking_data):
        """ позитивная проверка с использованием PUT """
        booking_id, create_response = self.create_booking(auth_session, booking_data)

        # Обновляем бронирование с помощью PUT
        updated_booking_data = booking_data.copy()
        updated_booking_data["firstname"] = faker.first_name()
        updated_booking_data["lastname"] = faker.last_name()
        updated_booking_data["totalprice"] = faker.random_int(min=100, max=400),
        updated_booking_data["additionalneeds"] = "nothing special"

        update_response = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=updated_booking_data)
        assert update_response.status_code == 200, "Ошибка при обновлении букинга"

        # Проверяем обновленное бронирование
        get_response = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_response.status_code == 200
        assert get_response.json()["firstname"] == updated_booking_data["firstname"]
        assert get_response.json()["lastname"] == updated_booking_data["lastname"]

        # Удаляем бронирование
        self.delete_booking(auth_session, booking_id)

    def test_partial_update_booking(self, auth_session, booking_data):
        """ позитивная проверка с использованием PATCH """
        booking_id, create_response = self.create_booking(auth_session, booking_data)

        # Обновляем бронирование с помощью PATCH
        updated_booking_data = booking_data.copy()
        updated_booking_data["lastname"] = faker.last_name()

        update_response = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=updated_booking_data)
        assert update_response.status_code == 200, "Ошибка при обновлении букинга"

        # Проверяем обновленное бронирование
        get_response = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_response.status_code == 200
        assert get_response.json()["firstname"] == updated_booking_data["firstname"]
        assert get_response.json()["lastname"] == updated_booking_data["lastname"]

        # Удаляем бронирование
        self.delete_booking(auth_session, booking_id)

    def test_get_all_bookings(self, auth_session):
        """ Позитивная проверка для получения всех бронирований """
        get_response = auth_session.get(f"{BASE_URL}/booking")

        # Проверяем, что ответ успешный
        assert get_response.status_code == 200, "Ошибка при получении списка бронирований"

        # Получаем данные из ответа
        bookings = get_response.json()

        # Проверяем, что ответ - это список
        assert isinstance(bookings, list), "Ответ должен быть в виде списка"
        print(get_response.json())

        # Если в списке есть хотя бы одно бронирование
        if bookings:
            for booking in bookings:
                # Проверяем, что каждый элемент в списке является словарем, содержащим ключ 'bookingid'
                assert "bookingid" in booking, "Каждое бронирование должно содержать 'bookingid'"

                # Проверяем, что поля 'firstname', 'lastname' могут быть отсутствующими, если их нет
                if "firstname" in booking:
                    assert isinstance(booking["firstname"], str), "Firstname должен быть строкой"
                if "lastname" in booking:
                    assert isinstance(booking["lastname"], str), "Lastname должен быть строкой"
                if "totalprice" in booking:
                    assert isinstance(booking["totalprice"], int), "Totalprice должен быть целым числом"
                if "additionalneeds" in booking:
                    assert isinstance(booking["additionalneeds"], str), "Additionalneeds должно быть строкой"

        else:
            print("Нет бронирований на данный момент.")
    # negative checks
    def test_update_booking_with_invalid_data(self, auth_session, booking_data):
        """ негативная проверка / передаем в одно из полей некорректное значение (int вместо str) """
        booking_id, create_response = self.create_booking(auth_session, booking_data)

        # Пример с некорректными данными, например, пустым обязательным полем
        invalid_data = booking_data.copy()
        invalid_data["firstname"] = 12345

        update_response = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=invalid_data)
        assert update_response.status_code == 500, "Ошибка 500: Плохой запрос, невалидные данные"

    def test_update_booking_without_token(self, auth_session, booking_data):
        """ негативная проверка / отсутствие авторизационного токена """
        # Создаем бронирование
        create_response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_response.status_code == 200, "Ошибка при создании бронирования"
        booking_id = create_response.json().get("bookingid")
        assert booking_id is not None, "ID бронирования не найден в ответе"

        # Создаем новый сессионный объект без токена (удаляем токен из заголовков)
        session_without_token = requests.Session()
        session_without_token.headers.update(HEADERS)

        # Попытка обновить бронирование без токена
        update_response = session_without_token.put(f"{BASE_URL}/booking/{booking_id}", json=booking_data)

        # Проверка, что ответ возвращает ошибку 401 (неавторизованный доступ)
        assert update_response.status_code == 403, "Негативная проверка / отсутсвие токена, запрос должен вернуть статус 403"

    def test_get_booking_with_nonexistent_id(self, auth_session):
        """ Негативная проверка для получения бронирования с несуществующим ID """
        nonexistent_booking_id = 9999
        get_response = auth_session.get(f"{BASE_URL}/booking/{nonexistent_booking_id}")
        assert get_response.status_code == 404, f"Бронирование с ID {nonexistent_booking_id} не должно существовать"
