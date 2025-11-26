import pytest
import requests
from utils.helpers import CLICKUP_API_KEY
from tests.api.conftest import BASE_URL, HEADERS
import allure

# новый коммит
@allure.feature('Создать задачу')
def test_create_task():
    with allure.step('Данные для задачи'):
        task_data = {
            "name": "[AUTO] Временная задача для теста",
            "description": "Создана автоматическим тестом. Будет удалена.",
            "status": "to do"
        }
    with allure.step('Отправить запрос'):
        list_id = '901517313290'
        response = requests.post(f'{BASE_URL}/list/{list_id}/task', headers=HEADERS, json=task_data)
        assert response.status_code == 200
        task = response.json()
        task_id = task["id"]
    with allure.step('Удалить созданную задачу'):
        delete = requests.delete(f'{BASE_URL}/task/{task_id}', headers=HEADERS)
    with allure.step('Проверить статус код'):
        assert delete.status_code == 204

@allure.feature('Получение данных')
def test_get_task(create_task):
    task_id = create_task
    with allure.step('Получить данные задачи'):
        response = requests.get(f'{BASE_URL}/task/{task_id}', headers=HEADERS)
    with allure.step('Проверить статус код'):
        assert response.status_code == 200

@allure.feature('Обновить данные задачи')
def test_update_task(create_task):
    task_data = {
        "name": 'AUTO to TEST',
        "description": "Создана автоматическим тестом. NO Будет удалена.",
        "status": "to do"
    }
    task_id = create_task
    with allure.step('Запрос на обновление'):
        resp = requests.put(f'{BASE_URL}/task/{task_id}', headers=HEADERS, json=task_data)
    with allure.step('Проверить статус код'):
        assert resp.status_code == 200

@allure.feature('Удалить задачу')
def test_delete_task(create_task):
    task_id = create_task
    with allure.step('Запрос на удаление'):
        response = requests.delete(f'{BASE_URL}/task/{task_id}', headers=HEADERS)
    with allure.step('Проверить статус код'):
        assert response.status_code == 204

@allure.feature('Создание задачи с неправильным ID')
def test_invalid_create_task():
    with allure.step('неправильный ID'):
        list_id = '901517313290'
    with allure.step('Создать задачу с неправильным ID'):
        response = requests.post(f'{BASE_URL}/list{list_id}', json={"name":""}, headers=HEADERS)
    with allure.step('Проверить статус код'):
        assert response.status_code == 404

@allure.feature('Получить данные задачи с негативным ID')
def test_get_invalid_task():
    with allure.step('неправильный id'):
        invalid_id = 99999
    with allure.step('Запрос на получение данных'):
        response = requests.get(f'{BASE_URL}/task/{invalid_id}', headers=HEADERS)
    with allure.step('Проверить статус код'):
        assert response.status_code == 401

@allure.feature('Обновить задачу с неправильным ID')
def test_update_invalid_task():
    with allure.step('неправильный id'):
        list_invalid_id = 99999
    with allure.step('данные'):
        task_data = {
            "name": 'AUTO to TEST',
            "description": "Создана автоматическим тестом. Будет удалена.",
            "status": "to go DO"
        }
    with allure.step('Запрос на обновление'):
        response = requests.put(f'{BASE_URL}/list{list_invalid_id}/task')
    with allure.step('Проверить статус код'):
        assert response.status_code == 404

@allure.feature('Удалить задачу с неправильным ID')
def test_delete_invalid_test():
    with allure.step('неверный id'):
        task_id = 1234
    with allure.step('запрос на удаление'):
        response = requests.delete(f'{BASE_URL}/task{task_id}', headers=HEADERS)
    with allure.step('Проверить статус код'):
        assert response.status_code == 404

