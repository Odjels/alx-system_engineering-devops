#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import json
import requests
import sys


def empl_todo_list():
    employee_id = int(sys.argv[1])
    empl_url1 = 'https://jsonplaceholder.typicode.com/users/%s' % employee_id
    empl_url2 = '%s/todo' % empl_url1
    todo_list = requests.get(empl_url2).json()
    empl = requests.get(empl_url1).json()
    complete_todo = []
    for todos in todo_list:
        if todos.get('completed') is True:
            complete_todo.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}): "
          .format(empl.get('name'), len(complete_todo), len(todo_list)))
    for todo in complete_todo:
        print("\t {}".format(todo))


if __name__ == '__main__':
    todo_list = empl_todo_list()
