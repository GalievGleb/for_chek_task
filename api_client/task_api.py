import requests
from utils.helpers import API_KEY

BASE = "https://api.clickup.com/api/v2"
HEADERS = {"Authorization": API_KEY}

def create_task(list_id: str, name: str) -> str:
    resp = requests.post(
        f"{BASE}/list/{list_id}/task",
        headers=HEADERS,
        json={"name": name}
    )
    assert resp.status_code == 200, f"Create failed: {resp.text}"
    return resp.json()["id"]

def delete_task(task_id: str) -> None:
    resp = requests.delete(f"{BASE}/task/{task_id}", headers=HEADERS)
    assert resp.status_code in (200, 404), f"Delete failed: {resp.status_code}"