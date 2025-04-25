from faker import Faker
from constants import headers, base_url
import requests
import pytest
from clickup.utils.helpers import CLICKUP_EMAIL, CLICKUP_PASSWORD, CLICKUP_API_KEY

faker = Faker()


@pytest.fixture(scope='session')
def auth_session():
    session = requests.Session()

    # Добавляем заголовки, включая API ключ
    session.headers.update({
        **headers,
        "Authorization": CLICKUP_API_KEY  # или f"Bearer {CLICKUP_API_KEY}" если нужно
    })

    response = session.post(f"{base_url}/auth", json={
        "username": CLICKUP_EMAIL,
        "password": CLICKUP_PASSWORD
    })

    assert response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session
