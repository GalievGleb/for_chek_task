from faker import Faker
from constant import BASE_URL, HEADERS
import requests

faker = Faker()

class TestBooking:
    def test_create_booking(auth_session, booking_data, create_booking, delete_booking):
        """Проверка создания данных"""
        # Создаем бронирование через фикстуру
        booking_id, create_response = create_booking  # Фикстура уже возвращает кортеж, мы просто распаковываем его

        # Проверка созданного бронирования
        assert create_response["booking"]["firstname"] == booking_data["firstname"]
        assert create_response["booking"]["lastname"] == booking_data["lastname"]
        assert create_response["booking"]["totalprice"] == booking_data["totalprice"]
        assert create_response["booking"]["additionalneeds"] == booking_data["additionalneeds"]

        # Удаляем бронирование через фикстуру
        delete_booking(booking_id)

    def test_full_update_booking(self, auth_session, booking_data, create_booking, delete_booking):
        """Проверка полного обновления данных"""
        # Создаем бронирование через фикстуру
        booking_id, create_response = create_booking

        # Обновляем бронирование с помощью PUT
        updated_booking_data = booking_data.copy()
        updated_booking_data["firstname"] = faker.first_name()
        updated_booking_data["lastname"] = faker.last_name()
        updated_booking_data["totalprice"] = faker.random_int(min=100, max=400)
        updated_booking_data["additionalneeds"] = "nothing special"

        update_response = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=updated_booking_data)
        assert update_response.status_code == 200, "Ошибка при обновлении букинга"

        # Проверяем обновленное бронирование
        get_response = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_response.status_code == 200
        assert get_response.json()["firstname"] == updated_booking_data["firstname"]
        assert get_response.json()["lastname"] == updated_booking_data["lastname"]

        # Удаляем бронирование через фикстуру
        delete_booking(booking_id)

    def test_partial_update_booking(self, auth_session, booking_data, create_booking, delete_booking):
        """Проверка частичного обновления данных"""
        # Создаем бронирование через фикстуру
        booking_id, create_response = create_booking

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

        # Удаляем бронирование через фикстуру
        delete_booking(booking_id)

    def test_get_all_bookings(self, auth_session):
        """Получение всех бронирований"""
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
    def test_update_booking_with_invalid_data(self, auth_session, booking_data, create_booking, delete_booking):
        """Проверка поведения системы при передачи в одно из полей некорректное значение (int вместо str)"""
        # Создаем бронирование через фикстуру
        booking_id, create_response = create_booking

        # Пример с некорректными данными, например, пустым обязательным полем
        invalid_data = booking_data.copy()
        invalid_data["firstname"] = 12345  # Некорректное значение

        update_response = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=invalid_data)
        assert update_response.status_code == 500, "Ошибка 500: Плохой запрос, невалидные данные"

        # Удаляем бронирование после теста
        delete_booking(booking_id)

    def test_update_booking_without_token(self, auth_session, booking_data, create_booking, delete_booking):
        """Проверка поведения системы при отсутствии авторизационного токена"""
        # Создаем бронирование через фикстуру
        booking_id, create_response = create_booking

        # Создаем новый сессионный объект без токена (удаляем токен из заголовков)
        session_without_token = requests.Session()
        session_without_token.headers.update(HEADERS)

        # Попытка обновить бронирование без токена
        update_response = session_without_token.put(f"{BASE_URL}/booking/{booking_id}", json=booking_data)

        # Проверка, что ответ возвращает ошибку 403 (неавторизованный доступ)
        assert update_response.status_code == 403, "Негативная проверка / отсутствие токена, запрос должен вернуть статус 403"

        # Удаляем бронирование после теста
        delete_booking(booking_id)

    def test_get_booking_with_nonexistent_id(self, auth_session, delete_booking):
        """Попытка получения бронирования с несуществующим ID"""
        nonexistent_booking_id = 9999
        get_response = auth_session.get(f"{BASE_URL}/booking/{nonexistent_booking_id}")
        assert get_response.status_code == 404, f"Бронирование с ID {nonexistent_booking_id} не должно существовать"
