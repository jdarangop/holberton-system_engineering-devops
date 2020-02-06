#!/usr/bin/python3
""" Module 0 """
import sys
from requests import get
import csv


if __name__ == "__main__":
    data = get('https://jsonplaceholder.typicode.com/users/{}'
               .format(sys.argv[1])).json()
    request = get('https://jsonplaceholder.typicode.com/todos/?userId={}'
                  .format(sys.argv[1]))
    all_tasks = request.json()
    with open('{}.csv'.format(sys.argv[1]), 'w') as f:
        csv_file = csv.writer(f)
        for task in all_tasks:
            csv_file.writerow([task.get('userId'),
                              data.get('name'),
                              task.get('completed'),
                              task.get('title')])
