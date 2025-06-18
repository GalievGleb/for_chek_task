import allure
import pytest
from clickup.api_clients.task_api import ClickUpTaskAPI


class TestTasks:
    def setup_method(self):
        self.task_api = ClickUpTaskAPI

    @allure.description("Проверка успешного создания задачи")
    def test_create_task(self):
        with allure.step("Создание задачи через API"):
            response = self.task_api.create_task("Create Task Test", "desc")
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка, что в ответе есть ID и имя"):
            json_data = response.json()
            assert "id" in json_data and json_data["id"], "Поле 'id' пустое"
            assert json_data["name"] == "Create Task Test"
        with allure.step("Удаление созданной задачи"):
            self.task_api.delete_task(json_data["id"])


    @allure.description("Проверка получения задачи по ID")
    def test_get_task(self, task_id_fixture):
        task_id = task_id_fixture
        with allure.step(f"Получение задачи с ID: {task_id}"):
            response = self.task_api.get_task(task_id)
        with allure.step("Проверка кода ответа и ID"):
            assert response.status_code == 200, f"Ошибка получения: {response.text}"
            assert response.json()["id"] == task_id


    @allure.description("Проверка обновления задачи")
    def test_update_task(self, task_id_fixture):
        task_id = task_id_fixture
        with allure.step("Обновление задачи"):
            response = self.task_api.update_task(task_id, "Updated Name")
        with allure.step("Проверка успешности обновления"):
            assert response.status_code == 200, f"Ошибка обновления: {response.text}"
            assert response.json()["name"] == "Updated Name", "Имя не обновилось"


    @allure.description("Проверка удаления задачи")
    def test_delete_task(self):
        with allure.step("Создание задачи для удаления"):
            response = self.task_api.create_task("Task to Delete", "Delete this task")
            task_id = response.json()["id"]
        with allure.step("Удаление задачи"):
            resp = self.task_api.delete_task(task_id)
        with allure.step("Проверка успешности удаления"):
            assert resp.status_code == 204


    @allure.description("Негативный тест: создание задач с невалидными данными")
    @pytest.mark.parametrize("bad_payload", [
        {"name": ""},
        {"description": "no name"},
        {},
    ])
    def test_create_task_negative_parametrized(self, bad_payload):
        with allure.step(f"Попытка создать задачу с невалидными данными: {bad_payload}"):
            response = self.task_api.create_task(**bad_payload)
        with allure.step("Проверка, что задача не была создана"):
            assert response.status_code != 200


    @allure.description("Негативный тест: получение несуществующей задачи")
    def test_get_task_negative(self):
        with allure.step("Получение задачи с невалидным ID"):
            response = self.task_api.get_task("invalid_task_id")
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 401


    @allure.description("Негативный тест: обновление задачи с невалидным ID")
    def test_update_task_negative(self):
        with allure.step("Обновление задачи с невалидным ID"):
            response = self.task_api.update_task("invalid_task_id", "fail")
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 401


    @allure.description("Негативный тест: удаление задачи с невалидным ID")
    def test_delete_task_negative(self):
        with allure.step("Удаление задачи с невалидным ID"):
            response = self.task_api.delete_task("invalid_task_id")
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 401