import requests
import logging
from module_4.task_2.config.constant import BASE_URL, AUTH_HEADERS, AUTH_DATA
class TestAuth:
    """
    Набор тестов, проверяющих корректность выдачи токена и обработки ошибок авторизации.

    Включает проверки следующих статусов:
    - отсутствии авторизационного токена (401 Unauthorized);
    - некорректных параметрах авторизации (422 Unprocessable Entity);
    - обращении к несуществующему ресурсу (404 Not Found);
    """
    def test_get_token(self, auth_session: requests.Session) -> None:
        """
        Проверяет успешное создание авторизованной сессии.

        Убедитесь, что фикстура auth_session возвращает объект requests.Session с установленным токеном.
        """
        assert auth_session is not None, "Не удалось создать сессию с токеном"
        logging.info("Токен успешно получен и добавлен в сессию.")

    def test_get_404(self, auth_session: requests.Session) -> None:
        """
        Проверяет, что при запросе к несуществующему ресурсу возвращается статус 404.
        """
        non_existent_url = f"{BASE_URL}/api/v1/non-existent-resource"
        response = auth_session.get(non_existent_url)

        assert response.status_code == 404, f"Ожидался статус код 404, но получен {response.status_code}"
        logging.info(f"Ответ на запрос к несуществующему ресурсу: {response.status_code}")

    def test_get_401_without_token(self) -> None:
        """
        Проверяет, что при отсутствии токена возвращается статус 401.
        """
        session = requests.Session()
        response = session.get(f"{BASE_URL}/api/v1/items/")
        assert response.status_code == 401, f"Ожидался статус код 401, но получен {response.status_code}"
        logging.info(f"Ответ 401 подтверждён: {response.status_code}")

    def test_post_422_invalid_login_data(self) -> None:
        """
        Проверяет, что при отправке некорректных данных в авторизацию возвращается статус 422.
        """
        session = requests.Session()

        invalid_data = AUTH_DATA.copy()
        invalid_data.pop('password', None)  # Удаляем ключ 'password'

        response = session.post(f"{BASE_URL}/api/v1/login/access-token", data=invalid_data, headers=AUTH_HEADERS)
        assert response.status_code == 422, f"Ожидался статус код 422, но получен {response.status_code}"
        logging.info(f"Ответ 422 подтверждён: {response.status_code}")

    def test_login_with_invalid_email_format_does_not_return_500(self) -> None:
        """
        Проверяет, что при попытке авторизации с некорректным password
        сервер не возвращает 500 Internal Server Error.
        """
        session = requests.Session()

        invalid_data = AUTH_DATA.copy()
        invalid_data['password'] = 'qwerty'  # имитация пароля с ошибкой

        response = session.post(f"{BASE_URL}/api/v1/login/access-token", data=invalid_data, headers=AUTH_HEADERS)

        assert response.status_code < 500, (
            f"Некорректный формат email не должен приводить к 500. Получен статус: {response.status_code}"
        )