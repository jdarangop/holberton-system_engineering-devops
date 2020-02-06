#!/usr/bin/python3
""" Module 0 """
import sys
from requests import get
import json


if __name__ == "__main__":
    data = get('https://jsonplaceholder.typicode.com/users').json()
    answer = {}
    for i in data:
        request = get('https://jsonplaceholder.typicode.com/todos/?userId={}'
                      .format(i.get('id')))
        all_tasks = request.json()
        answer.update({i.get('id'): [{"task": task.get('title'),
                                     "completed": task.get('completed'),
                      "username": i.get('name')}
                                     for task in all_tasks]})
    with open('todo_all_employees.json', 'w') as f:
        f.write(json.dumps(answer))
