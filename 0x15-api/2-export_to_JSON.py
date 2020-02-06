#!/usr/bin/python3
""" Module 2 """
import json
from requests import get
import sys


if __name__ == "__main__":
    data = get('https://jsonplaceholder.typicode.com/users/{}'
               .format(sys.argv[1])).json()
    request = get('https://jsonplaceholder.typicode.com/todos/?userId={}'
                  .format(sys.argv[1]))
    all_tasks = request.json()
    answer = {sys.argv[1]: [{"task": task.get('title'),
              "completed": task.get('completed'),
                            "username": data.get('name')}
                            for task in all_tasks]}
    with open('{}.json'.format(sys.argv[1]), 'w') as f:
        f.write(json.dumps(answer))
