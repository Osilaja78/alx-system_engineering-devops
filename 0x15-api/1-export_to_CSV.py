#!/usr/bin/python3
"""
This script gathers data from an API and exports
it to a CSV file.
"""


import json
import requests
import sys


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

    content = ""
    for data in loaded_todo_data:
        content += '"{}","{}","{}","{}"\n'.format(
            user_id,
            name,
            data['completed'],
            data['title']
        )

    with open(f'{user_id}.csv', 'w', encoding='UTF8') as f:
        f.write(content)
