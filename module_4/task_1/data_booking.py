from typing import Dict, Any
from faker import Faker

faker = Faker()

def generate_booking_data() -> Dict[str, Any]:
    """
    Генерирует словарь с данными бронирования.

    Returns:
        dict: Словарь, содержащий информацию о бронировании.
    """
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
