import requests
from requests import session

from module_4.fast_api.constant.constant import BASE_URL, HEADERS


class Test_auth():
    def test_auth_session(self, auth_session):

        get_me_response = auth_session.get(f"{BASE_URL}/api/v1/users/me")
        assert get_me_response.status_code == 200

        get_items_response = auth_session.get(f"{BASE_URL}/api/v1/items/?skip=0&limit=5")
        assert get_items_response.status_code == 200
        print(get_items_response.json())