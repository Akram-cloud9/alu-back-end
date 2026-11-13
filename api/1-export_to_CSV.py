#!/usr/bin/python3
"""Export an employee's TODO list to CSV."""

import csv
import json
import sys
import urllib.request


def main():
    """Retrieve employee tasks and write them to a CSV file."""
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

    with open('{}.csv'.format(employee_id), 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                employee_id,
                user.get('username'),
                task.get('completed'),
                task.get('title')
            ])


if __name__ == "__main__":
    main()
