#!/usr/bin/python3
"""Gather data from an API"""


import requests
import sys


def get_todo_list_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch employee data
        employee_response = requests.get(employee_url)
        employee_response.raise_for_status()
        employee_data = employee_response.json()

        # Fetch TODO list data
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
        todo_data = todo_response.json()

        # Extract relevant information
        employee_name = employee_data["name"]
        completed_tasks = [task for task in todo_data if task["completed"]]
        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(todo_data)

        # Display information
        print(
            f"Employee {employee_name} is done with tasks(
                {number_of_done_tasks}/{total_number_of_tasks}): ")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_list_progress(employee_id)
