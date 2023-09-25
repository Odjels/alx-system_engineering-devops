#!/usr/bin/python3
""" This module gathers data from an API """

import csv
import json
import requests
import sys


def empl_todo_list():
    employee_id = int(sys.argv[1])
    empl_url1 = 'https://jsonplaceholder.typicode.com/users/%s' % employee_id
    empl_url2 = '%s/todos' % empl_url1
    todo_list = requests.get(empl_url2).json()
    empl = requests.get(empl_url1).json()
    path = "{}.csv".format(employee_id)

    with open(path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for t in todo_list:
            writer.writerow([employee_id, empl.get('username'),
                            t.get('completed'), t.get('title')])


if __name__ == '__main__':
    empl_todo_list()
