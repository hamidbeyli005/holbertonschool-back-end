#!/usr/bin/python3
"""Export data in the CSV format"""

import csv
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

filename = '{}.csv'.format(employee_id)
with open(filename, mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_ALL)
    for todo in todos:
        writer.writerow([employee_id, employee['username'],
                        todo['completed'], todo['title']])
