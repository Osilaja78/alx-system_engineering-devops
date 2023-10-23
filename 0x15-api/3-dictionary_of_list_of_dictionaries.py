#!/usr/bin/python3
"""
This script gathers data from an API and
exports it to a JSON file.
"""


import json
import requests


if __name__ == '__main__':

    base_url = "https://jsonplaceholder.typicode.com"
    request_user_url = f"{base_url}/users"

    res = requests.get(request_user_url)
    data = res.text

    loaded_data = json.loads(data)

    content_dict = {}
    for data in loaded_data:

        user_id = data.get('id')
        name = data.get('name')

        content_dict[user_id] = []

        request_todo_url = f"{base_url}/todos?userId={user_id}"

        todo_res = requests.get(request_todo_url)
        todo_data = todo_res.text
        loaded_todo_data = json.loads(todo_data)

        for todo_data in loaded_todo_data:
            content = {
                "task": todo_data['title'],
                "completed": todo_data['completed'],
                "username": name
            }
            content_dict[user_id].append(content)

    dumped_content = json.dumps(content_dict)

    with open(f'todo_all_employees.json', 'w', encoding='UTF8') as f:
        f.write(dumped_content)
