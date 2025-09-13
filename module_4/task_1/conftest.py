import requests
import pytest
from faker import Faker
from typing import Tuple, Dict, Generator, Callable
from constant import USERNAME, PASSWORD, HEADERS, BASE_URL
from data_booking import generate_booking_data

faker = Faker()


@pytest.fixture(scope="session")
def auth_session() -> requests.Session:
    """
    Создаёт и возвращает сессию с авторизацией.

    Returns:
        requests.Session: Сессия с авторизацией и установленными заголовками.
    """
    session = requests.Session()
    session.headers.update(HEADERS)

    auth_response = session.post(
        f"{BASE_URL}/auth",
        headers=HEADERS,
        json={"username": USERNAME, "password": PASSWORD}
    )
    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture()
def booking_data() -> Dict:
    """
    Генерирует и возвращает данные бронирования.

    Returns:
        dict: Словарь с данными бронирования.
    """
    return generate_booking_data()


@pytest.fixture
def create_booking(auth_session: requests.Session, booking_data: Dict) -> Tuple[int, Dict]:
    """
    Создаёт бронирование и возвращает его ID и данные ответа.

    Args:
        auth_session (requests.Session): Авторизованная сессия.
        booking_data (dict): Данные бронирования.

    Returns:
        tuple: (ID бронирования, данные ответа в формате JSON)
    """
    create_response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    assert create_response.status_code == 200, "Ошибка при создании бронирования"
    booking_id = create_response.json().get("bookingid")
    assert booking_id is not None, "ID бронирования не найден в ответе"
    return booking_id, create_response.json()


@pytest.fixture
def delete_booking(auth_session: requests.Session) -> Generator[Callable[[int], None], None, None]:
    """
    Возвращает функцию удаления бронирования по ID.

    Args:
        auth_session (requests.Session): Авторизованная сессия.

    Yields:
        Callable[[int], None]: Функция, принимающая booking_id и удаляющая бронирование.
    """

    def _delete_booking(booking_id: int) -> None:
        delete_response = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_response.status_code == 201, f"Ошибка при удалении бронирования с ID {booking_id}"
        check_delete_response = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert check_delete_response.status_code == 404, f"Бронирование с ID {booking_id} не было удалено"

    yield _delete_booking
