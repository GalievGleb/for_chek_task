from utils.helpers import CLICKUP_API_KEY

BASE_URL  = "https://api.clickup.com/api"
LIST_ID = '901510425948'
LIST_NAME = 'List Autotest'
HEADERS = {
    "accept": "application/json",
    "Authorization": CLICKUP_API_KEY
}
PRIORITY_LIST = ['Low', 'Normal', 'Urgent', 'High']
name_wrong_type = (({"name": 123}), ({"name": [123]}), ({"name": True}), ({"name": ""}), ({"name": None}))