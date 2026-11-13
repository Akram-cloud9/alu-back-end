#!/usr/bin/python3
"""Export an employee's TODO list to JSON."""

import json
import sys
import urllib.request


def main():
    """Retrieve employee tasks and write them to a JSON file."""
    employee_id = int(sys.argv[1])

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id
    )
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        employee_id
    )

    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode('utf-8'))

    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode('utf-8'))

    task_list = []

    for task in todos:
        task_list.append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user.get('username')
        })

    data = {str(employee_id): task_list}

    with open('{}.json'.format(employee_id), 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    main()
