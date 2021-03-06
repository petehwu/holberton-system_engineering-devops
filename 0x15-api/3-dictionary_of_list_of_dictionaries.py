#!/usr/bin/python3
"""This script goes out to a REST API and gets some information
and writes as json to file
"""
import json
from collections import OrderedDict
import requests
import sys

if __name__ == '__main__':

    uri = "https://jsonplaceholder.typicode.com"
    res = requests.get("{}/users".format(uri))
    outer = OrderedDict()
    for user in res.json():
        uid = str(user.get('id'))
        payload = {"userId": uid}
        tasks = requests.get("{}/todos".format(uri), params=payload)
        username = user.get("username")
        rows = []
        for t in tasks.json():
            new_dict = OrderedDict()
            new_dict['username'] = username
            new_dict['task'] = t.get("title")
            new_dict['completed'] = t.get("completed")
            rows.append(new_dict)
        outer[uid] = rows
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(outer, jsonfile)
