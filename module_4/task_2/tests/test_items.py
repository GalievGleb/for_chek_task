from module_4.task_2.config.constant import BASE_URL, HEADERS



def create_item(auth_session, item_data):
    """Создание нового item"""
    create_response = auth_session.post(f"{BASE_URL}/api/v1/items/", json=item_data, headers=HEADERS)
    assert create_response.status_code == 200, "Ошибка при создании item"

    created_item = create_response.json()
    assert "id" in created_item, "ID item не найден"
    assert created_item["title"] == item_data["title"], "Название не совпадает"
    assert created_item["description"] == item_data["description"], "Описание не совпадает"

    return created_item  # Возвращаем созданный элемент с ID
def delete_item(auth_session, item_id):
    """Удаление item по ID"""
    delete_response = auth_session.delete(f"{BASE_URL}/api/v1/items/{item_id}", headers=HEADERS)
    assert delete_response.status_code == 200, f"Ошибка при удалении item с ID {item_id}"

    # Проверяем, что item был удален
    check_delete_response = auth_session.get(f"{BASE_URL}/api/v1/items/{item_id}", headers=HEADERS)
    assert check_delete_response.status_code == 404, f"Item с ID {item_id} не был удален"
def delete_all_items(auth_session):
    """Вспомогательная функция для удаления всех созданных постов"""

    # Получаем список всех постов
    response = auth_session.get(f"{BASE_URL}/api/v1/items/", headers=HEADERS)
    assert response.status_code == 200, f"Ошибка при получении списка постов: {response.status_code}"

    # Получаем данные как JSON
    try:
        response_data = response.json()  # Преобразуем ответ в Python-объект
    except ValueError:
        raise Exception("Не удалось преобразовать ответ в JSON")

    # Проверяем, есть ли поле 'data', которое содержит список постов
    if 'data' in response_data:
        items = response_data['data']  # Берем список постов из поля 'data'

        # Удаляем каждый пост
        for item in items:
            # Убедитесь, что item - это словарь и содержит ключ 'id'
            if isinstance(item, dict) and 'id' in item:
                item_id = item['id']  # ID поста - строка
                delete_response = auth_session.delete(f"{BASE_URL}/api/v1/items/{item_id}", headers=HEADERS)
                assert delete_response.status_code == 200, f"Ошибка при удалении поста с ID {item_id}"
                print(f"Пост с ID {item_id} был удален")
            else:
                print(f"Невалидный элемент данных для удаления: {item}")
    else:
        print("Нет поля 'data' в ответе. Невозможно удалить посты.")


# CRUD actions
def test_create_delete_item(auth_session, random_item_data):
    """Тест для создания, проверки и удаления item"""

    # Создаем item с использованием функции
    item_data = random_item_data
    created_item = create_item(auth_session, item_data)

    # Проверяем, что item существует
    item_id = created_item["id"]
    get_response = auth_session.get(f"{BASE_URL}/api/v1/items/{item_id}", headers=HEADERS)
    assert get_response.status_code == 200, "Ошибка при получении item"
    item_data_from_get = get_response.json()
    assert item_data_from_get["id"] == item_id, "ID item не совпадает"

    # Удаляем item
    delete_item(auth_session, item_id)  # Удаление через функцию

def test_full_update_item(auth_session, random_item_data):
    """Тест для создания, проверки, обновления и удаления item"""

    # Создаем новый item с использованием функции
    item_data = random_item_data
    created_item = create_item(auth_session, item_data)

    # Получаем ID созданного элемента
    item_id = created_item["id"]

    # Данные для обновления элемента
    updated_item_data = {
        "title": "Updated Title",
        "description": "Updated description"
    }

    # Обновляем элемент через PUT запрос
    update_response = auth_session.put(f"{BASE_URL}/api/v1/items/{item_id}", json=updated_item_data, headers=HEADERS)
    assert update_response.status_code == 200, f"Ошибка при обновлении item с ID {item_id}"

    # Проверяем, что элемент был обновлен
    get_updated_response = auth_session.get(f"{BASE_URL}/api/v1/items/{item_id}", headers=HEADERS)
    assert get_updated_response.status_code == 200, f"Ошибка при получении обновленного item с ID {item_id}"
    updated_item = get_updated_response.json()
    assert updated_item["title"] == updated_item_data["title"], "Название не обновилось"
    assert updated_item["description"] == updated_item_data["description"], "Описание не обновилось"

    # Удаляем элемент
    delete_item(auth_session, item_id)  # Удаление через функцию

def test_partial_update_item(auth_session, random_item_data):
    """Тест для создания, частичного обновления, проверки и удаления item"""

    # Создаем новый item с использованием функции
    item_data = random_item_data
    created_item = create_item(auth_session, item_data)

    # Получаем ID созданного элемента
    item_id = created_item["id"]

    # Данные для частичного обновления элемента
    partial_updated_item_data = {
        "title": "тест-проверка patch"  # Обновляем только поле title
    }

    # Частичное обновление элемента через PATCH запрос
    patch_response = auth_session.patch(f"{BASE_URL}/api/v1/items/{item_id}", json=partial_updated_item_data, headers=HEADERS)
    assert patch_response.status_code == 200, f"Ошибка при частичном обновлении item с ID {item_id}"

    # Проверяем, что элемент был частично обновлен
    get_updated_response = auth_session.get(f"{BASE_URL}/api/v1/items/{item_id}", headers=HEADERS)
    assert get_updated_response.status_code == 200, f"Ошибка при получении обновленного item с ID {item_id}"
    updated_item = get_updated_response.json()

    # Проверяем, что только title было обновлено
    assert updated_item["title"] == partial_updated_item_data["title"], "Название не обновилось"
    # Ожидаем, что описание останется прежним (поскольку мы не обновляли его)
    assert updated_item["description"] == item_data["description"], "Описание было изменено, хотя не должно было"

    # Удаляем элемент
    # delete_item(auth_session, item_id)

def test_check_pagination(auth_session, random_item_data):
    """Тест для проверки пагинации при создании 20 items"""

    # Очистка всех существующих элементов
    delete_all_items(auth_session)

    # Создаем 20 items
    # for i in range(20):
    #     item_data = random_item_data
    #     create_response = auth_session.post(f"{BASE_URL}/api/v1/items/", json=item_data, headers=HEADERS)
    #     assert create_response.status_code == 200, f"Ошибка при создании item #{i + 1}: {create_response.status_code}"
    #
    #     created_item = create_response.json()
    #     assert "id" in created_item, f"ID item #{i + 1} не найден в ответе"
    #     print(f"Item #{i + 1} успешно создан")
    #
    # # Теперь отправим запрос для получения всех элементов с пагинацией (например, страница 1)
    # response = auth_session.get(f"{BASE_URL}/api/v1/items?page=1", headers=HEADERS)
    # assert response.status_code == 200, "Ошибка при получении данных с пагинацией"
    #
    # # Выводим структуру ответа
    # response_data = response.json()
    # pprint.pprint(response_data)  # Выводим красивую структуру JSON для отладки
def test_get_all_items(auth_session):
    """Тест для получения всех items и вывода их в консоль"""

    # отправляем GET запрос для получения всех items с нужными заголовками
    get_response = auth_session.get(f"{BASE_URL}/api/v1/items/")

    # проверяем, что запрос выполнен успешно
    assert get_response.status_code == 200, f"Ошибка при получении списка items: {get_response.status_code}"

    items = get_response.json()
    print(f"Items: {items}")


