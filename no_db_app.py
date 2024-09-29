from flask import Flask, render_template, request, redirect, url_for, Response, jsonify

app: Flask = Flask(__name__)

# In-memory list to store tasks
tasks: list = []

@app.route(rule = '/',  methods=['GET'])
def index() -> str:
     tmp : str = render_template('index.html', tasks=tasks)
     return tmp   

@app.route( rule = '/add', methods=['POST'])
def add_task() -> Response:
    task: str = request.form.get('task')
    if task:
        tasks.append(task)
    response: Response = redirect(url_for('index'))
    return response


@app.route(rule= '/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id) -> Response:
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    tmp: Response =  jsonify({"status": "success", "task_id": task_id}), 200
    return tmp

if __name__ == '__main__':
    app.run(debug=True)
