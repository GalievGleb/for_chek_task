import pytest
import requests
from playwright.sync_api import sync_playwright
import allure
from faker import Faker

from clickup.helpers.utils import CLICKUP_EMAIL, CLICKUP_PASSWORD
from clickup.pages.login_page import LoginPage
from clickup.tests.constant import BASE_URL, HEADERS

fake = Faker()


@allure.feature("Фикстуры инициализации")
@pytest.fixture(scope="session")
def browser():
    with allure.step("Запуск браузера Chromium"):
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False, slow_mo=300)
    yield browser
    with allure.step("Завершение работы браузера"):
        browser.close()
        playwright.stop()


@allure.feature("Генерация тестовых данных")
@pytest.fixture()
def task_data_generator():
    with allure.step("Генерация данных для задачи"):
        return fake.sentence()


@allure.feature("Авторизация")
@pytest.fixture(scope="session")
def login(browser):
    with allure.step("Создание новой страницы"):
        page = browser.new_page()
    login_page = LoginPage(page)
    with allure.step("Авторизация на сайте через UI"):
        login_page.login(CLICKUP_EMAIL, CLICKUP_PASSWORD)
    yield page
    with allure.step("Закрытие страницы после теста"):
        page.close()


@pytest.fixture()
@allure.title("Фикстура удаления задач")
def delete_task_fixture(task_id):
    def _delete_task():
        with allure.step(f"Удаление задачи через API (ID: {task_id})"):
            url = f"{BASE_URL}/v2/task/{task_id}"
            response = requests.delete(url, headers=HEADERS)
            with allure.step(f"Проверка статуса удаления: {response.status_code}"):
                pass
            return response
    return _delete_task


