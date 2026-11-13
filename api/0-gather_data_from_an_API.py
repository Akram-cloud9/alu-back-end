#!/usr/bin/python3
"""Gather employee TODO list progress from a REST API."""

import json
import sys
import urllib.request


def main():
    """Display an employee's completed TODO tasks."""
    employee_id = int(sys.argv[1])

    user_url = (
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(employee_id)
    )
    todos_url = (
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(employee_id)
    )

    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode('utf-8'))

    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode('utf-8'))

    employee_name = user.get('name')
    completed_tasks = [
        task for task in todos if task.get('completed')
    ]
    total_tasks = len(todos)

    print(
        'Employee {} is done with tasks({}/{}):'.format(
            employee_name, len(completed_tasks), total_tasks
        )
    )

    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))


if __name__ == "__main__":
    main()

