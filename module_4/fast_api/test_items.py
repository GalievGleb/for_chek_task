import requests
from requests import session, delete

from module_4.fast_api.conftest import auth_session, item_data
from module_4.fast_api.constant.constant import BASE_URL, HEADERS

class Test_items():
    def test_create_item(self,item):
        """Проверка что item был создан"""
        assert "id" in item
        assert  "title" in item
        assert "description" in item

    def test_get_item(self,auth_session,item):
        """Получение списка items"""
        response = auth_session.get(f"{BASE_URL}/api/v1/items/")
        assert response.status_code == 200
        items = response.json()["data"]
        ids = [i["id"] for i in items]
        assert item["id"] in ids

    def test_update_item(self,auth_session,item, put_item_data):
        """Изменение созданого item"""
        item_id = item["id"]
        print(item_id)
        response = auth_session.put(f"{BASE_URL}/api/v1/items/{item_id}", json=put_item_data)
        assert response.status_code == 200
        response = auth_session.get(f"{BASE_URL}/api/v1/items/{item_id}")
        update_item = response.json()
        assert update_item["title"] == put_item_data["title"]
        assert update_item["description"] == put_item_data["description"]



