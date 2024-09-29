# Flask To-Do List Application

This is a simple to-do list application built with Flask and SQLite.

## Overview
This Flask application allows users to manage a to-do list by adding and deleting tasks. The tasks are stored in an SQLite database.

## Dependencies
- **Flask**: A micro web framework for Python.
- **Flask-SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy.
- **Typing**: For type hints.

## Configuration
- **Database URI**: The SQLite database is configured with the URI `'sqlite:///todo.db'`.
- **Track Modifications**: Disabled to avoid overhead.

## Models
- **Task**: Represents a to-do task with two fields:
  - `id`: An integer primary key.
  - `content`: A string to store the task content.

## Routes
- **`/` (index)**:
  - **Method**: `GET`
  - **Description**: Fetches all tasks from the database and renders them using the `index.html` template.
  - **Returns**: Rendered HTML page.

- **`/add`**:
  - **Method**: `POST`
  - **Description**: Adds a new task to the database.
  - **Returns**: Redirects to the index page.

- **`/delete/<int:task_id>`**:
  - **Method**: `DELETE`
  - **Description**: Deletes a task from the database based on the task ID.
  - **Returns**: JSON response with the status and task ID.

## Example Usage
1. **Run the Application**:
   ```bash
   python app.py
