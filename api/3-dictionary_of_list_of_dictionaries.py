#!/usr/bin/python3

import json
import requests


def export_to_json():
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    user_tasks = {}
    for user in users:
        user_tasks[user['id']] = []
        for task in todo:
            if task['userId'] == user['id']:
                task_dict = {
                    'username': user['username'],
                    'task': task['title'],
                    'completed': task['completed']
                }
                user_tasks[user['id']].append(task_dict)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file)


if __name__ == "__main__":
    export_to_json()
