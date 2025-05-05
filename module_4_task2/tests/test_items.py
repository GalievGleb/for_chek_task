import pytest
from module_4_task2.config.const import AUTH_HEADERS, BASE_URL, AUTH_DATA, API_HEADERS


class TestItems:
    endpoint = f"{BASE_URL}/api/v1/items/"

    def test_create_item(self, item_data, auth_session):
        response = auth_session.post(self.endpoint, json=item_data)
        data = response.json()
        item_id = data.get("id")
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"
        assert "id" in data
        assert item_id is not None
        assert data["title"] == item_data["title"]


    def test_get_items(self, auth_session):
        response = auth_session.get(self.endpoint)
        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"
        data = response.json()
        assert "data" in data, "Нет ключа 'data'"
        assert isinstance(data["data"], list), "'data' должен быть списком"
        assert isinstance(data.get("count"), int), " ключ 'count' должен быть целым число"
        assert data["count"] >=20 , f"Количество элементов меньше 20: {data['count']}"

    def test_update_items(self, auth_session, item_data,update_item):
        response = auth_session.post(self.endpoint, json=item_data)
        item_id = response.json().get('id')
        put_update = auth_session.put(f'{self.endpoint}{item_id}', json=update_item)
        assert put_update.status_code == 200, 'Данные не изменились'
        assert put_update.json()["title"] == update_item["title"], 'title не изменился'
        assert put_update.json()["description"] == update_item["description"], 'description не изменился'

    def test_delete_item(self,auth_session,item_data):
        response = auth_session.post(self.endpoint, json=item_data)
        item_id = response.json().get('id')
        del_item = auth_session.delete(f'{self.endpoint}{item_id}')
        assert del_item.status_code == 200

        # пробуем удалить повторно
        del_again = auth_session.delete(f"{self.endpoint}{item_id}")
        assert del_again.status_code == 404

    # def test_20creat(self,auth_session, update_item ):
    #     for i in range(20):
    #         creat_items = auth_session.post(f'{BASE_URL}/api/v1/items/', json=update_item)
    #         assert creat_items.status_code == 200, 'Не создалось 20 итемов'