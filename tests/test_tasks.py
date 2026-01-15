# tests/test_tasks.py
import json
from src.app import app

def test_create_task_success():
    client = app.test_client()
    payload = {
        "title": "Planejar sprint",
        "description": "Definir metas e tarefas",
        "priority": "High",
        "status": "To Do",
        "owner": "Ana",
        "due_date": "2026-01-20"
    }
    resp = client.post("/tasks", data=json.dumps(payload), content_type="application/json")
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["title"] == "Planejar sprint"
    assert data["priority"] == "High"
    assert data["due_date"] == "2026-01-20"

def test_list_tasks_filter_by_priority():
    client = app.test_client()
    resp = client.get("/tasks?priority=High")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)

def test_update_task_not_found():
    client = app.test_client()
    resp = client.put("/tasks/999", data=json.dumps({"status": "Done"}), content_type="application/json")
    assert resp.status_code == 404
