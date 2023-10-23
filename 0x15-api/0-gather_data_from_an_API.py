#!/usr/bin/python3
"""This script gathers data from an API"""


import sys
import requests
import json


if __name__ == '__main__':

    base_url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    request_user_url = f"{base_url}/users?id={user_id}"
    request_todo_url = f"{base_url}/todos?userId={user_id}"

    res = requests.get(request_user_url)
    data = res.text

    loaded_data = json.loads(data)
    name = loaded_data[0].get('name')

    todo_res = requests.get(request_todo_url)
    todo_data = todo_res.text
    loaded_todo_data = json.loads(todo_data)

    total_tasks = len(loaded_todo_data)

    completed_tasks = []
    for data in loaded_todo_data:
        if data.get('completed'):
            completed_tasks.append(data)

    total_completed_tasks = len(completed_tasks)

    print(f"Employee {name} is done with "
          f"tasks({total_completed_tasks}/{total_tasks})")

    for task in completed_tasks:
        print(f"\t {task.get('title')}")
