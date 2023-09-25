#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import json
import requests
import sys


if __name__ == "__main__":
    empl_url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(empl_url)
    result = requests.get(user)
    json_empl = result.json()
    dis_task = {}
    for user in json_empl:
        name = user.get('username')
        userid = user.get('id')
        todos = '{}todos?userId={}'.format(empl_url, userid)
        result = requests.get(todos)
        tasks = result.json()
        lst_task = []
        for task in tasks:
            dic_task = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            lst_task.append(dic_task)

        dis_task[str(userid)] = lst_task
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(dis_task, f)
