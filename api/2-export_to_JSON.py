#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests
import sys

if len(sys.argv) < 2:
    print('Usage: {} <employee_id>'.format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]

# Fetch employee data
response = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
employee = response.json()

# Fetch todo data
response = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id))
todos = response.json()

filename = '{}.json'.format(employee_id)
data = {employee_id: []}
for todo in todos:
    data[employee_id].append({
        "task": todo['title'],
        "completed": todo['completed'],
        "username": employee['username']
    })

with open(filename, mode='w') as file:
    json.dump(data, file)
