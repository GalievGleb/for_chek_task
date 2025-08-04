import pytest
import requests
from constant import ITEM_URL


class TestItems:
    def test_get_items(self, auth_session):
        """ Получает список элементов
        args:
            фикстура auth_session: хранит сессию авторизации
        asserts:
            1.Проверка статус кода после получения всех элементов
            2.Проверка, есть ли ключ "data"
            3.Проверка, является ли data списком
            4.Проверка, "count" является ли числом
        """
        response = auth_session.get(ITEM_URL)
        assert response.status_code == 200, f"Ошибка запроса: {response.status_code}, {response.json().get('detail')}"

        data = response.json()
        assert "data" in data, "В ответе отсутствует ключ 'data'"
        assert isinstance(data["data"], list), "'data' не является списком"
        assert isinstance(data.get("count"), int), "'count' должен быть целым числом"

    def test_update_item(self, auth_session, create_item: str):
        """ Обновление существующего элемента по ID
        args:
            фикстура auth_session: хранит сессию авторизации
            фикстура create_item: хранит предусловие - создание элемента и постусловие - удаление элемента
        asserts:
            1.Проверка статус кода после получения конкретного элемента
            2.Проверка статус кода после обновления элемента
            3.Проверка, изменились ли данные в элементе
        """
        data_for_update = {"title": "New_word", "description": "New_description"}

        response = auth_session.get(create_item)
        data_before_update = response.json()
        assert response.status_code == 200, f"Ошибка запроса: {response.status_code}, {response.json().get('detail')}"

        response = auth_session.put(create_item, json=data_for_update)
        data_after_update = response.json()
        assert response.status_code == 200, f"Ошибка запроса: {response.status_code}, {response.json().get('detail')}"
        assert data_before_update.get("title") != data_after_update.get("title")

    def test_double_delete_item(self, auth_session):
        """ Удаляет несуществующий элемент(двойное удаление)

        args:
            фикстура auth_session: хранит сессию авторизации
        assert:
            1.Проверка стутуса кода после создания элемента
            2.Проверка статуса кода после удаления элемента
            3.Проверка статуса кода после удаления несуществующего элемента
        """
        response = auth_session.post(url=ITEM_URL, json={"title": "New_word", "description": "New_description"})
        item_id = response.json().get("id")
        assert response.status_code == 200, f"Элемент не создался: {response.status_code}"

        response = auth_session.delete(ITEM_URL+item_id)
        assert response.status_code == 200, f"Элемент с ID: {item_id} - не удалился"

        response = auth_session.delete(ITEM_URL + item_id)
        assert response.status_code == 404, f"Ошибка удаление элемента: {response.status_code}, элемент удалился дважды"

    def test_create_items_invalid_data(self, auth_session):
        """ Созданаёт элемент с невалидными данными

        args:
            фикстура auth_session: хранит сессию авторизации

        assert:
            Проверка статус кода после отправки невалидных данных
        """
        invalid_data = {
            "data": [
                {"title": "A"*256, "description": "A"*256},
                {"title": "", "description": None},
                {"title": 1, "description": 2}
            ]
        }
        for data in invalid_data:
            response = auth_session.post(ITEM_URL, json=data)
            assert response.status_code == 422, f"Отправка невалидных данных прошла успешна:{response.json().get('detail')}"

    def test_update_non_existent_item(self, auth_session):
        """ Обновление несуществующего элемента

        args:
            фикстура auth_session: хранит сессию авторизации

        assert:
            Проверка статус кода, после обновления несуществующего элемента
        """
        response = auth_session.put(ITEM_URL + "random_item123", json={"title": "a", "description": "a"})
        assert response.status_code == 422, f"Несуществующий элемент обновился: {response.status_code}"

