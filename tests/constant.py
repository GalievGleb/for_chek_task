from clickup.helpers.utils import CLICKUP_API_KEY

BASE_URL  = "https://api.clickup.com/api"
LIST_NAME = 'Project 2'
HEADERS = {
    "content-type": "application/json",
    "Authorization": CLICKUP_API_KEY
}


DATA = {
        "name": "Test Task",
        "description": "Test description"
    }