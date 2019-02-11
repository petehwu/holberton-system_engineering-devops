#!/usr/bin/python3
"""This script goes out to a REST API and gets some information
"""
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
        uid = res.json()
        comp = []
        tot = 0
        for val in tasks.json():
            tot += 1
            if val.get("completed"):
                comp.append("\t {}".format(val.get("title")))
        print("Employee {} is done with tasks({}/{}):".
              format(uid.get('name'), len(comp), tot))
        print(*comp, sep="\n")
