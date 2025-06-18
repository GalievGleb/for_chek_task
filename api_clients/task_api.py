import requests
from clickup.tests.constant import BASE_URL, HEADERS
from clickup.helpers.utils import CLICKUP_LIST_ID

class ClickUpTaskAPI:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def create_task(name=None, description=None):
        # Создать задачу через API
        response = requests.post(f"{BASE_URL}/v2/list/{CLICKUP_LIST_ID}/task",json= {
            "name": name,
            "description": description
        }, headers=HEADERS)
        return response


    def get_task(task_id):
        # Получить задачу по ID через API
        url = f"{BASE_URL}/v2/task/{task_id}"
        response = requests.get(url, headers=HEADERS)
        return response


    def update_task(task_id, name=None, description=None):
        # Обновить задачу через API
        url = f"{BASE_URL}/v2/task/{task_id}"
        data = {}  # Словарь для обновляемых полей
        if name:
            data["name"] = name  # Добавляем имя задачи, если передано
        if description:
            data["description"] = description  # Добавляем описание, если передано
        response = requests.put(url, json=data, headers=HEADERS)
        return response


    def delete_task(task_id):
        # Удалить задачу через API
        url = f"{BASE_URL}/v2/task/{task_id}"
        response = requests.delete(url, headers=HEADERS)
        return response
