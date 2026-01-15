from flask import Flask, request, jsonify
from .repository import TaskRepository

app = Flask(__name__)
repo = TaskRepository()

# Rota inicial
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "TechFlow Task Manager API está rodando!"}), 200

# Listar tarefas (com filtro opcional por prioridade)
@app.route("/tasks", methods=["GET"])
def list_tasks():
    priority = request.args.get("priority")
    tasks = repo.list_tasks(priority=priority)
    return jsonify(tasks), 200

# Obter uma tarefa específica
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = repo.get_task(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200

# Criar nova tarefa
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    required = ["title", "description", "priority", "status", "owner", "due_date"]
    missing = [k for k in required if k not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400
    task = repo.create_task(data)
    return jsonify(task), 201

# Atualizar tarefa existente
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    updated = repo.update_task(task_id, data)
    if not updated:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(updated), 200

# Deletar tarefa
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    deleted = repo.delete_task(task_id)
    if not deleted:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Task deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
