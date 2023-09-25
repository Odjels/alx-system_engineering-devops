#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import json
import requests
import sys


if __name__ == "__main__":
    empl_url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user = '{}users/{}'.format(empl_url, userid)
    result = requests.get(user)
    json_empl = result.json()
    name = json_empl.get('username')

    todos = '{}todos?userId={}'.format(empl_url, userid)
    result = requests.get(todos)
    tasks = result.json()
    lst_task = []
    for task in tasks:
        dic_task = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": name}
        lst_task.append(dic_task)

    dis_task = {str(userid): lst_task}
    filename = '{}.json'.format(userid)
    with open(filename, mode='w') as f:
        json.dump(dis_task, f)
