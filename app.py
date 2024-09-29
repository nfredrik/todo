from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from typing import Tuple

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db : SQLAlchemy= SQLAlchemy(app=app)

# Create a Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index() -> str:
    tasks: Task = Task.query.all()
    result: str = render_template(template_name_or_list='index.html', tasks=tasks)
    return result

@app.route('/add', methods=['POST'])
def add_task() -> Response:
    task_content :str = request.form.get(key='task')
    if task_content:
        new_task : Task = Task(content=task_content)
        db.session.add(instance=new_task)
        db.session.commit()
    response : Response =  redirect(location=url_for('index'))
    return response

@app.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id) -> Response:
    task : Task = Task.query.get(task_id)
    if task:
        db.session.delete(instance=task)
        db.session.commit()
    response : Response =  jsonify({"status": "success", "task_id": task_id})
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)
