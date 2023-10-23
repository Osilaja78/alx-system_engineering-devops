#!/usr/bin/python3
"""
This script gathers data from an API and
exports it to a JSON file.
"""


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

    content_dict = {user_id: []}
    for data in loaded_todo_data:
        content = {
            "task": data['title'],
            "completed": data['completed'],
            "username": name
        }
        content_dict[user_id].append(content)

    dumped_content = json.dumps(content_dict)

    with open(f'{user_id}.json', 'w', encoding='UTF8') as f:
        f.write(dumped_content)
