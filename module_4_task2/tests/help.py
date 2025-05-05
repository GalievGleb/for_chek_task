import requests
from module_4_task2.config.const import AUTH_HEADERS, BASE_URL, AUTH_DATA, API_HEADERS
from faker import Faker
fake1 = Faker()


def creat ():
    session = requests.Session()
    for i in range(20):
        data = {
        "title": fake1.word().capitalize(),
        "description": fake1.sentence(nb_words=10)
    }
        creat_items = session.post(f'{BASE_URL}/api/v1/items/', json = data)
        assert creat_items.status_code == 200, 'Не создалось 20 итемов'
