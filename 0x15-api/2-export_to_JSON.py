#!/usr/bin/python3
"""This script goes out to a REST API and gets some information
and then write to file as json
"""
import json
from collections import OrderedDict
import requests
import sys

if __name__ == '__main__':

    if (len(sys.argv) != 2):
        print("Error: Usage ./0-gather_data_from_an_API.py <employee Id>")
    elif not sys.argv[1].isnumeric():
        print("Error: employee ID must be an integer")
    else:
        uri = "https://jsonplaceholder.typicode.com"
        res = requests.get("{}/users/{}".format(uri, sys.argv[1]))
        payload = {"userId": sys.argv[1]}
        tasks = requests.get("{}/todos".format(uri), params=payload)
        user = res.json()
        username = user.get("username")
        rows = []
        for t in tasks.json():
            new_dict = OrderedDict()
            new_dict['task'] = t.get("title")
            new_dict['completed'] = t.get("completed")
            new_dict['username'] = username
            rows.append(new_dict)
        with open('{}.json'.format(str(sys.argv[1])), 'w') as jsonfile:
            json.dump({sys.argv[1]: rows}, jsonfile)
