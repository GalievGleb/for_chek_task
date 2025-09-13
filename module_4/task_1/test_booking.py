from typing import Tuple, Dict, Any, Callable
from faker import Faker
from constant import BASE_URL, HEADERS
import requests
import pytest

faker = Faker()

class TestBooking:
    """
    Набор автотестов для проверки CRUD-операций над сущностью 'booking'.

    Сценарии включают:
    - Позитивные проверки создания, полного и частичного обновления, получения и удаления бронирования.
    - Негативные сценарии, такие как обновление с невалидными данными, отсутствие токена и запрос несуществующего ID.
    """

    @pytest.mark.positive
    def test_create_booking(
            self,
            auth_session: requests.Session,
            booking_data: Dict[str, Any],
            create_booking: Tuple[int, Dict[str, Any]],
            delete_booking: Callable[[int], None]
    ) -> None:
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

    @pytest.mark.positive
    def test_full_update_booking(
        self,
        auth_session: requests.Session,
        booking_data: Dict[str, Any],
        create_booking: Tuple[int, Dict[str, Any]],
        delete_booking: Callable[[int], None]
    ) -> None:
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

    @pytest.mark.positive
    def test_partial_update_booking(
        self,
        auth_session: requests.Session,
        booking_data: Dict[str, Any],
        create_booking: Tuple[int, Dict[str, Any]],
        delete_booking: Callable[[int], None]
    ) -> None:
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

    @pytest.mark.positive
    def test_get_all_bookings(self, auth_session: requests.Session) -> None:
        """Позитивный тест: получение всех бронирований"""

        response = auth_session.get(f"{BASE_URL}/booking")
        assert response.status_code == 200, "Ошибка при получении списка бронирований"

        bookings = response.json()
        assert isinstance(bookings, list), "Ответ должен быть в виде списка"

        if not bookings:
            pytest.skip("Нет доступных бронирований для проверки")

        for booking in bookings:
            assert isinstance(booking, dict), "Каждое бронирование должно быть словарем"
            assert "bookingid" in booking, "Каждое бронирование должно содержать 'bookingid'"

            expected_types = {
                "firstname": str,
                "lastname": str,
                "totalprice": int,
                "additionalneeds": str,
            }

            for field, expected_type in expected_types.items():
                if field in booking:
                    assert isinstance(booking[field], expected_type), \
                        f"{field} должно быть типа {expected_type.__name__}"


    @pytest.mark.negative
    def test_update_booking_with_invalid_data(
        self,
        auth_session: requests.Session,
        booking_data: Dict[str, Any],
        create_booking: Tuple[int, Dict[str, Any]],
        delete_booking: Callable[[int], None]
    ) -> None:
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

    @pytest.mark.negative
    def test_update_booking_without_token(
        self,
        auth_session: requests.Session,
        booking_data: Dict[str, Any],
        create_booking: Tuple[int, Dict[str, Any]],
        delete_booking: Callable[[int], None]
    ) -> None:
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

    @pytest.mark.negative
    def test_get_booking_with_nonexistent_id(self, auth_session: requests.Session) -> None:
        """Попытка получения бронирования с несуществующим ID"""
        nonexistent_booking_id = 9999
        get_response = auth_session.get(f"{BASE_URL}/booking/{nonexistent_booking_id}")
        assert get_response.status_code == 404, f"Бронирование с ID {nonexistent_booking_id} не должно существовать"
