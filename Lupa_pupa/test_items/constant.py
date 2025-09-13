BASE_URL = "https://api.pomidor-stage.ru"
LOGIN_URL = f"{BASE_URL}/api/v1/login/access-token"
ITEM_URL = f"{BASE_URL}/api/v1/items/"

AUTH_HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

API_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

AUTH_DATA = {
    "username": "gleb.g30.06@mail.ru",
    "password": "glebg3006",
    "scope": "",
    "client_id": "",
    "client_secret": ""
}



