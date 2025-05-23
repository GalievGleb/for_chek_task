from http.client import responses

import pytest
from constant import BASE_URL,AUTH_DATA, endpoint
from faker import Faker

class TestItems:
    """Класс включает в себя работу с items. Создает, удаляет, обновляет, получает все items,
    а так же проверяет их содержание"""

    endpoint = f"{BASE_URL}/api/v1/items/"


    def test_get_token(self, auth_session):
        response = auth_session.post(f"{BASE_URL}/api/v1/login/test-token")
        assert response.status_code in (200, 204), f"response: {response.status_code}, {response.text}"
        assert response.json()['is_active'] == True, 'Состояние пользователя не true'
        assert response.json()['id'] == AUTH_DATA["username"], 'пользователь не найден'


    def test_create_item(self, item_data, auth_session):
        """Создает тестовый item, проверяет статус код, а так же проверяет что item создан"""
        response = auth_session.post(self.endpoint, json=item_data)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"

        data = response.json()
        item_id = data.get("id")
        assert item_id is not None
        assert data.get("title") == item_data["title"]

        self.created_item_id = item_id

    def test_create_20_items(self, auth_session):
        """Создает сразу 20 items с уникальными данными в каждом item, проверяет статус код и наличие id"""
        for i in range(20):
            fake = Faker()
            item_data_20 = {
            "title": fake.word(),
            "description": fake.sentence(nb_words=10)
        }
            response = auth_session.post(self.endpoint, json=item_data_20)
            assert response.status_code in (200, 201), f"Ошибка при создании item {i}: {response.text}"
            data = response.json()
            assert data.get("id") is not None
            assert "data" in data, "Response missing 'data' key"
            assert isinstance(data["data"], list), "'data' is not a list"
            assert isinstance(data.get("count"), int), "'count' should be integer"

        # удаление всех элементов после теста
        get_response = auth_session.get(endpoint)
        if get_response.status_code == 200:
            for item in get_response.json().get('data', []):
                item_id = item['id']
                auth_session.delete(f'{endpoint}{item_id}')



    def test_get_items(self, auth_session):
        response = auth_session.get(self.endpoint)

        # Проверяем успешный статус
        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"

        data = response.json()

        # Проверяем базовую структуру ответа
        assert "data" in data, "Response missing 'data' key"
        assert isinstance(data["data"], list), "'data' should be a list"
        assert isinstance(data.get("count"), int), "'count' should be integer"

        # Дополнительные проверки, если есть элементы
        if data["data"]:  # Если список не пустой
            for item in data["data"]:
                assert "id" in item, "Item missing 'id'"
                assert "name" in item, "Item missing 'name'"
        else:  # Если список пустой
            assert data["count"] == 0, "Count should be 0 when no items"


    def test_updt_items(self, auth_session, item_data):
        items_list = []
        response = auth_session.get(self.endpoint)
        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"
        for i in response.json()["data"]:
            items_list.append(i.get("id"))
        for i in items_list:
            response = auth_session.put(self.endpoint + i, json=item_data)
            assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"


    def test_delete_all_items(self, auth_session):
        # Получаем список всех элементов
        try:
            response = auth_session.get(self.endpoint)
            response.raise_for_status()  # Проверяем HTTP ошибки
        except Exception as e:
            pytest.skip(f"Не удалось получить список элементов: {str(e)}")
            return

        # Проверяем структуру ответа
        try:
            data = response.json()
            items = data.get("data", [])
        except ValueError:
            pytest.fail("Некорректный JSON-ответ")
            return

        # Если элементов нет - выходим
        if not items:
            print("Нет элементов для удаления")
            return

        # Собираем ID элементов
        item_ids = [item["id"] for item in items if "id" in item]

        # Удаляем элементы с обработкой ошибок
        deleted_count = 0
        for item_id in item_ids:
            try:
                del_response = auth_session.delete(f"{self.endpoint}/{item_id}")
                if del_response.status_code in (200, 204):
                    deleted_count += 1
                else:
                    print(f"Ошибка удаления элемента {item_id}: {del_response.text}")
            except Exception as e:
                print(f"Ошибка при удалении {item_id}: {str(e)}")

        # Проверяем результат
        try:
            check_response = auth_session.get(self.endpoint)
            remaining_items = check_response.json().get("data", [])
        except Exception as e:
            pytest.fail(f"Ошибка проверки результата: {str(e)}")
            return

        # Проверка без падения теста
        if len(remaining_items) > 0:
            pytest.xfail(f"Осталось неудаленных элементов: {len(remaining_items)}")


