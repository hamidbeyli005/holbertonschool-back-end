#!/usr/bin/python3
"""Gather data from an API"""


import requests
import sys

if len(sys.argv) < 2:
    print('Usage: {} <employee_id>'.format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]

# Fetch employee data
response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
employee = response.json()

# Fetch todo data
response = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id))
todos = response.json()

done_tasks = [task for task in todos if task['completed']]
total_tasks = len(todos)

print('Employee {} is done with tasks({}/{}):'.format(employee['name'], len(done_tasks), total_tasks))

for task in done_tasks:
    print('\t {}'.format(task['title']))