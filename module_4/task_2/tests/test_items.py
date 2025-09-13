from module_4.task_2.config.constant import BASE_URL, HEADERS
import pytest
import logging

# Настроим логирование
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class TestItems:
    """
    Набор тестов для проверки операций с объектами item через API.

    Включает:
    - создание, получение и удаление item;
    - полное обновление item;
    - проверку пагинации (наличия полей count, data)  при массовом создании элементов (20 шт);
    - получение списка всех item и вывод их в консоль.

    Тесты используют авторизованную сессию и вспомогательные фикстуры для генерации данных и управления объектами.
    """
    @pytest.mark.positive
    def test_create_delete_item(self, auth_session, random_item_data, create_item, delete_item):
        """Тест для создания, проверки и удаления item с использованием фикстур"""

        # Используем фикстуру для создания item
        created_item = create_item(auth_session, random_item_data)

        # Проверяем, что item существует
        item_id = created_item["id"]
        get_response = auth_session.get(f"{BASE_URL}/api/v1/items/{item_id}", headers=HEADERS)
        assert get_response.status_code == 200, "Ошибка при получении item"
        item_data_from_get = get_response.json()
        assert item_data_from_get["id"] == item_id, "ID item не совпадает"

        # Удаляем item через фикстуру
        delete_item(auth_session, item_id)  # Теперь передаем два аргумента

    @pytest.mark.positive
    def test_full_update_item(self, auth_session, random_item_data, create_item, delete_item):
        """Тест для полного обновления item"""

        # Используем фикстуру для создания item
        created_item = create_item(auth_session, random_item_data)

        # Получаем ID созданного элемента
        item_id = created_item["id"]

        # Данные для обновления элемента
        updated_item_data = {
            "title": "Updated Title",
            "description": "Updated description"
        }

        # Обновляем элемент через PUT запрос
        update_response = auth_session.put(f"{BASE_URL}/api/v1/items/{item_id}", json=updated_item_data,
                                           headers=HEADERS)
        assert update_response.status_code == 200, f"Ошибка при обновлении item с ID {item_id}"

        # Проверяем, что элемент был обновлен
        get_updated_response = auth_session.get(f"{BASE_URL}/api/v1/items/{item_id}", headers=HEADERS)
        assert get_updated_response.status_code == 200, f"Ошибка при получении обновленного item с ID {item_id}"
        updated_item = get_updated_response.json()
        assert updated_item["title"] == updated_item_data["title"], "Название не обновилось"
        assert updated_item["description"] == updated_item_data["description"], "Описание не обновилось"

        # Удаляем элемент через фикстуру
        delete_item(auth_session, item_id)

    @pytest.mark.positive
    def test_check_pagination(self, auth_session, random_item_data, create_item, delete_item):
        """Тест для проверки пагинации при создании 20 постов и их удаления"""

        # Создаем 20 постов
        created_items = []
        for i in range(20):
            created_item = create_item(auth_session, random_item_data)
            created_items.append(created_item)
            print(f"Создан пост {i + 1}")  # Выводим сообщение о созданном посте

        # Получаем список всех постов
        response = auth_session.get(f"{BASE_URL}/api/v1/items/", headers=HEADERS)
        assert response.status_code == 200, f"Ошибка при получении списка постов: {response.status_code}"

        # Проверяем, что в ответе есть поля 'count' и 'data'
        response_data = response.json()
        assert 'count' in response_data, "Поле 'count' не найдено в ответе"
        assert 'data' in response_data, "Поле 'data' не найдено в ответе"

        # Проверяем, что количество постов больше 20 (чтобы не затрагивать созданные вручную)
        assert response_data[
                   'count'] > 20, f"Ожидалось, что количество постов будет больше 20, но получено {response_data['count']}"

        # Проверяем, что в 'data' есть хотя бы один элемент
        assert len(response_data['data']) > 0, "В поле 'data' нет постов"

        # Удаляем созданные посты
        for item in created_items:
            delete_item(auth_session, item["id"])  # Удаление каждого созданного поста
            print(f"Удален пост с ID {item['id']}")

    @pytest.mark.positive
    def test_get_all_items(self, auth_session):
        """Тест для получения всех items и вывода их в консоль"""

        # отправляем GET запрос для получения всех items с нужными заголовками
        get_response = auth_session.get(f"{BASE_URL}/api/v1/items/", headers=HEADERS)

        # проверяем, что запрос выполнен успешно
        assert get_response.status_code == 200, f"Ошибка при получении списка items: {get_response.status_code}"

        items = get_response.json()

        # Логируем полученные items
        logger.info(f"Items: {items}")

        # Дополнительно можно вывести количество постов в консоль, если это нужно
        logger.info(f"Количество постов: {len(items.get('data', []))}")


