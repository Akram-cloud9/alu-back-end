#!/usr/bin/python3
"""Export all employees' TODO lists to JSON."""

import json
import urllib.request


def main():
    """Retrieve all employees and their tasks."""
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    with urllib.request.urlopen(users_url) as response:
        users = json.loads(response.read().decode('utf-8'))

    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode('utf-8'))

    all_tasks = {}

    for user in users:
        user_id = str(user.get('id'))
        username = user.get('username')
        user_tasks = []

        for task in todos:
            if task.get('userId') == user.get('id'):
                user_tasks.append({
                    'username': username,
                    'task': task.get('title'),
                    'completed': task.get('completed')
                })

        all_tasks[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    main()
