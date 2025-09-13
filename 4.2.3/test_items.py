import pytest
from constant import BASE_URL
from faker import Faker

class TestItems:
    endpoint = f"{BASE_URL}/api/v1/items/"

    def test_create_item(self, item_data, auth_session):
        response = auth_session.post(self.endpoint, json=item_data)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"

        data = response.json()
        item_id = data.get("id")
        assert item_id is not None
        assert data.get("title") == item_data["title"]

        self.created_item_id = item_id

    def test_create_20_items(self, auth_session):
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

    def test_get_items(self, auth_session):
        response = auth_session.get(self.endpoint)
        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert "data" in data, "Response missing 'data' key"
        assert isinstance(data["data"], list), "'data' is not a list"
        assert isinstance(data.get("count"), int), "'count' should be integer"

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
        items_list = []
        response = auth_session.get(self.endpoint)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"
        for i in response.json()["data"]:
            items_list.append(i.get("id"))
        for i in items_list:
            response = auth_session.delete(self.endpoint + i)
            assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"

        get_check_response = auth_session.get(f"{BASE_URL}/api/v1/items/")
        assert len(get_check_response.json().get("data")) == 0, 'Не все данные удалены!'


