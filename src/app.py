# src/app.py
from flask import Flask, request, jsonify
from .repository import TaskRepository

app = Flask(__name__)
repo = TaskRepository()

@app.route("/tasks", methods=["GET"])
def list_tasks():
    priority = request.args.get("priority")
    tasks = repo.list_tasks(priority=priority)
    return jsonify(tasks), 200

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    required = ["title", "description", "priority", "status", "owner"]
    if not all(k in data for k in required):
        return jsonify({"error": "Missing fields"}), 400
    task = repo.create_task(data)
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    updated = repo.update_task(task_id, data)
    if not updated:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(updated), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    deleted = repo.delete_task(task_id)
    if not deleted:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
