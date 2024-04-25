#!/usr/bin/python3
"""
Python script that, using REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv


def gather_user_information():
    """
    Fethces and processes user and TODO list data for the provided ID.
    """
    Id = argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{Id}'
    tasks_url = f'https://jsonplaceholder.typicode.com/todos?userId={Id}'

    user = json.loads(requests.get(user_url).text)
    tasks = json.loads(requests.get(tasks_url).text)

    completed_tasks = []
    completed = 0
    employee_name = user['name']

    for task in tasks:
        if task['completed'] is True:
            completed += 1
            completed_tasks.append(task['title'])

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          completed,
                                                          len(tasks)))
    for title in completed_tasks:
        print(f"\t {title}")


if __name__ == "__main__":
    if len(argv) == 2:
        gather_user_information()
