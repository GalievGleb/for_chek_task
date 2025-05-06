import allure
import pytest
from config.constants import BASE_URL, LIST_ID, LIST_NAME
from utils.helpers import CLICKUP_EMAIL, MY_ID, USERNAME, get_initials, check_tag
from tests.conftest import delete_task

class TestTasks:
    import allure

    @allure.feature("Создание задач")
    @allure.story("Создание задачи с привязкой к родителю и валидацией полей")
    @allure.title("Тест на создание задачи с полной валидацией")
    def test_create_task(self, create_task_factory, generate_create_task_data, auth_session):
        with allure.step("Создаем родительскую задачу"):
            parent_task = create_task_factory()[0].get('id')

        with allure.step("Генерируем данные для задачи с parent_task"):
            test_data = generate_create_task_data(parent_task)

        with allure.step("Создаем основную задачу"):
            response = create_task_factory(test_data)[0]

        with allure.step("Проверяем поля основной задачи"):
            assert response.get('id'), 'id не вернулось в ответе'
            assert response.get('name') == test_data['name'], 'name таски из запроса не совпадает с name в ответе'
            assert response.get('description') == test_data['description'], 'description таски из запроса не совпадает с description в ответе'
            assert response.get('status')['status'] == test_data['status'], 'text_content таски из запроса не совпадает с text_content в ответе'

        with allure.step("Проверяем данные создателя"):
            assert response.get('creator')['email'] == CLICKUP_EMAIL, 'email создателя таски не совпадает'
            assert response.get('creator')['id'] == int(MY_ID), 'id создателя таски не совпадает'
            assert response.get('creator')['username'] == USERNAME, 'Имя создателя не совпадает'

        with allure.step("Проверяем приоритет задачи"):
            assert response.get('priority')['id'] == str(test_data['priority']), 'Приоритет не совпадает'

        with allure.step("Проверяем массив watchers"):
            watcher = response.get('watchers')[0]
            assert watcher['id'] == int(MY_ID), 'id watcher не совпадает'
            assert watcher['username'] == USERNAME, 'Имя watcher не совпадает'
            assert watcher['email'] == CLICKUP_EMAIL, 'email watcher не совпадает'
            assert watcher['initials'] == get_initials(USERNAME), 'initials watcher не совпадают'

        with allure.step("Проверяем родительскую связь задачи"):
            assert response.get('parent') == parent_task, 'id связанной таски не совпадает'
            assert response.get('top_level_parent') == parent_task, 'top_level_parent не совпадает'

        with allure.step("Проверяем список задачи"):
            assert response.get('list')['id'] == LIST_ID, 'id списка не совпадает'
            assert response.get('list')['name'] == LIST_NAME, 'Имя списка не совпадает'

        with allure.step("Проверяем назначенного исполнителей"):
            assignee = response.get('assignees')[0]
            assert assignee['id'] == int(MY_ID), 'id assignee не совпадает'
            assert assignee['username'] == USERNAME, 'Имя assignee не совпадает'
            assert assignee['email'] == CLICKUP_EMAIL, 'email assignee не совпадает'
            assert assignee['initials'] == get_initials(USERNAME), 'initials assignee не совпадают'

        with allure.step("Проверяем теги задачи"):
            assert check_tag(test_data['tags'], response.get('tags'), MY_ID), 'Теги не совпадают'

    import allure

    @allure.title("Обновление задачи")
    def test_update_task(self, create_task_factory, auth_session, generate_update_task_data):
        with allure.step("Создаем основную задачу"):
            task_id = create_task_factory()[0].get('id')

        with allure.step("Создаем родительскую задачу для связи"):
            parent_task = create_task_factory()[0].get('id')

        with allure.step("Генерируем данные для обновления задачи"):
            test_data = generate_update_task_data(parent_task)
            allure.attach(str(test_data), name="Тело запроса", attachment_type=allure.attachment_type.JSON)

        with allure.step("Отправляем PUT-запрос для обновления задачи"):
            response = auth_session.put(f'{BASE_URL}/v2/task/{task_id}', json=test_data)
            allure.attach(response.text, name="Ответ сервера", attachment_type=allure.attachment_type.JSON)
            assert response.status_code == 200, f"Ошибка выполнения запроса: {response.status_code}, {response.text}"
            response = response.json()

        with allure.step("Проверяем основные поля задачи"):
            with allure.step("Проверяем ID задачи"):
                assert task_id == response.get('id'), "ID задачи не совпадает"

            with allure.step("Проверяем name задачи"):
                assert response.get('name') == test_data['name'], "Имя задачи не совпадает"

            with allure.step("Проверяем описание задачи"):
                assert response.get('description') == test_data['description'], "Описание не совпадает"
                assert response.get('text_content') == test_data['description'], "Text content не совпадает"

            with allure.step("Проверяем статус задачи"):
                assert response.get('status')['status'] == test_data['status'], "Статус не совпадает"

        with allure.step("Проверяем поля создателя задачи"):
            assert response.get('creator')['email'] == CLICKUP_EMAIL, "Email создателя не совпадает"
            assert response.get('creator')['id'] == int(MY_ID), "ID создателя не совпадает"
            assert response.get('creator')['username'] == USERNAME, "Имя создателя не совпадает"

        with allure.step("Проверяем приоритет и связи задачи"):
            assert response.get('priority')['id'] == str(test_data['priority']), "Приоритет не совпадает"
            assert response.get('parent') == parent_task, "ID родительской задачи не совпадает"
            assert response.get('top_level_parent') == parent_task, "ID верхней задачи не совпадает"

        with allure.step("Проверяем корректность списка"):
            assert response.get('list')['id'] == LIST_ID, "ID списка не совпадает"
            assert response.get('list')['name'] == LIST_NAME, "Имя списка не совпадает"

    @allure.title("Получение информации о задаче")
    def test_get_task(self, auth_session, create_task_factory, generate_create_task_data):
        with allure.step("Создаем родительскую задачу"):
            parent_task = create_task_factory()[0].get('id')

        with allure.step("Генерируем данные для основной задачи с привязкой"):
            test_data = generate_create_task_data(parent_task)
            allure.attach(str(test_data), name="Тело запроса", attachment_type=allure.attachment_type.JSON)

        with allure.step("Создаем основную задачу"):
            task_id = create_task_factory(test_data)[0].get('id')

        with allure.step("Отправляем GET-запрос для получения задачи"):
            response = auth_session.get(f'{BASE_URL}/v2/task/{task_id}')
            allure.attach(response.text, name="Ответ сервера", attachment_type=allure.attachment_type.JSON)
            assert response.status_code == 200, f"Ошибка выполнения запроса: {response.status_code}, {response.text}"
            response = response.json()

        with allure.step("Проверяем основные поля задачи"):
            with allure.step("Проверка ID задачи"):
                assert task_id == response.get('id'), "ID задачи не совпадает"

            with allure.step("Проверка названия задачи"):
                assert response.get('name') == test_data['name'], "Название задачи не совпадает"

            with allure.step("Проверка описания задачи"):
                assert response.get('description') == test_data['description'], "Описание задачи не совпадает"
                assert response.get('text_content') == test_data['description'], "Text content не совпадает"

            with allure.step("Проверка статуса задачи"):
                assert response.get('status')['status'] == test_data['status'], "Статус задачи не совпадает"

            with allure.step("Проверка приоритета"):
                assert response.get('priority')['id'] == str(test_data['priority']), "Приоритет задачи не совпадает"

        with allure.step("Проверяем связи между задачами"):
            assert response.get('parent') == parent_task, "ID родительской задачи не совпадает"
            assert response.get('top_level_parent') == parent_task, "ID верхней задачи не совпадает"
            assert response.get('linked_tasks')[0]['task_id'] == parent_task, "Связанная задача не совпадает"

        with allure.step("Проверяем данные создателя"):
            creator = response.get('creator')
            assert creator['email'] == CLICKUP_EMAIL, "Email создателя не совпадает"
            assert creator['id'] == int(MY_ID), "ID создателя не совпадает"
            assert creator['username'] == USERNAME, "Имя создателя не совпадает"

        with allure.step("Проверяем данные исполнителя (assignees)"):
            assignee = response.get('assignees')[0]
            assert assignee['id'] == int(MY_ID), "ID исполнителя не совпадает"
            assert assignee['username'] == USERNAME, "Имя исполнителя не совпадает"
            assert assignee['email'] == CLICKUP_EMAIL, "Email исполнителя не совпадает"
            assert assignee['initials'] == get_initials(USERNAME), "Инициалы исполнителя не совпадают"

        with allure.step("Проверяем наблюдателей (watchers)"):
            watcher = response.get('watchers')[0]
            assert watcher['id'] == int(MY_ID), "ID наблюдателя не совпадает"
            assert watcher['username'] == USERNAME, "Имя наблюдателя не совпадает"
            assert watcher['email'] == CLICKUP_EMAIL, "Email наблюдателя не совпадает"
            assert watcher['initials'] == get_initials(USERNAME), "Инициалы наблюдателя не совпадают"

        with allure.step("Проверяем данные списка"):
            assert response.get('list')['id'] == LIST_ID, "ID списка не совпадает"
            assert response.get('list')['name'] == LIST_NAME, "Имя списка не совпадает"

        with allure.step("Проверяем теги задачи"):
            assert check_tag(test_data['tags'], response.get('tags'), MY_ID), "Теги не совпадают"


    @allure.title("Удаление задачи")
    def test_delete_task(self, auth_session, create_task_factory):
        task_id = create_task_factory()[0].get('id')

        with allure.step("Удаляем задачу"):
            delete_task(task_id, auth_session)

        with allure.step("Проверяем, что задача удалена и не доступна по GET"):
            response = auth_session.get(f'{BASE_URL}/v2/task/{task_id}')
            assert response.status_code == 404, f"Ошибка выполнения запроса: {response.status_code}, {response.text}"
            assert response.json().get('err') == 'Task not found, deleted', \
                f"Описание ошибки не совпадает: {response.json().get('err')}"


    @allure.title("Создание задачи с невалидным именем")
    @pytest.mark.parametrize("wrong_jsons", [{"name": 123}, {"name": [123]}, {"name": True}, {"name": ""}, {"name": None}])
    def test_create_task_invalid_name(self, auth_session, wrong_jsons):
        with allure.step(f"Отправляем POST запрос с невалидным именем: {wrong_jsons['name']}"):
            response = auth_session.post(f"{BASE_URL}/v2/list/{LIST_ID}/task", json=wrong_jsons)

        with allure.step("Проверяем код ответа и сообщение об ошибке"):
            assert response.status_code == 400, f"Ошибка выполнения запроса: {response.status_code}, {response.text}"
            assert response.json() == {'err': 'Task name invalid', 'ECODE': 'INPUT_005'}


    @allure.title("Создание задачи с невалидной датой")
    @pytest.mark.parametrize("wrong_jsons", [
        {"name": "Test", "due_date": "not_timestamp"},
        {"name": "Test", "due_date": "123abc"},
        {"name": "Test", "due_date": True},
        {"name": "Test", "due_date": [123]}
    ])
    def test_create_task_invalid_date(self, auth_session, wrong_jsons):
        with allure.step(f"Отправляем POST запрос с невалидной датой: {wrong_jsons['due_date']}"):
            response = auth_session.post(f"{BASE_URL}/v2/list/{LIST_ID}/task", json=wrong_jsons)

        with allure.step("Проверяем код ответа и сообщение об ошибке"):
            assert response.status_code == 400, f"Ошибка выполнения запроса: {response.status_code}, {response.text}"
            assert response.json() in ({'err': 'Due date not valid, must be positive', 'ECODE': 'ITEM_115'},
                                       {'err': 'Date invalid', 'ECODE': 'INPUT_006'})


    @allure.title("Получение задачи с невалидным ID")
    @pytest.mark.parametrize("wrong_id", [True, None, 'wrong', '', 999999999])
    def test_get_task_invalid(self, create_task_factory, auth_session, wrong_id):
        create_task_factory()  # Чтобы список задач не был пустым

        with allure.step(f"Отправляем GET запрос с некорректным ID: {wrong_id}"):
            response = auth_session.get(f'{BASE_URL}/v2/task/{wrong_id}')

        with allure.step("Проверяем код ответа и сообщение об ошибке"):
            assert response.status_code in (401, 404)
            assert response.json() in [
                {'err': 'Team not authorized', 'ECODE': 'OAUTH_027'},
                {'err': 'Route not found', 'ECODE': 'APP_001'}
            ]


    @allure.title("Обновление задачи с невалидным ID")
    @pytest.mark.parametrize("wrong_id", [True, None, 'wrong', 999999999])
    def test_update_task_invalid_id(self, auth_session, create_task_factory, wrong_id, generate_update_task_data):
        test_data = generate_update_task_data()
        create_task_factory()  # Чтоб не было пусто

        with allure.step(f"Отправляем PUT запрос с невалидным ID: {wrong_id}"):
            response = auth_session.put(f'{BASE_URL}/v2/task/{wrong_id}', json=test_data)

        with allure.step("Проверяем код ответа и сообщение об ошибке"):
            assert response.status_code == 401, f"Ошибка выполнения запроса: {response.status_code}, {response.text}"
            assert response.json() == {'err': 'Team not authorized', 'ECODE': 'OAUTH_027'}


    @allure.title("Удаление задачи с невалидным ID")
    @pytest.mark.parametrize("wrong_id", [True, None, 'wrong', 999999999])
    def test_delete_task_invalid(self, auth_session, create_task_factory, wrong_id):
        create_task_factory()

        with allure.step(f"Отправляем DELETE запрос с невалидным ID: {wrong_id}"):
            response = auth_session.delete(f'{BASE_URL}/v2/task/{wrong_id}')

        with allure.step("Проверяем код ответа и сообщение об ошибке"):
            assert response.status_code == 401, f"Ошибка выполнения запроса: {response.status_code}, {response.text}"
            assert response.json() == {'err': 'Team not authorized', 'ECODE': 'OAUTH_027'}


