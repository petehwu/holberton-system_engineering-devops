#!/usr/bin/python3
"""This script goes out to a REST API and gets some information then export
to csv
"""
import csv
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
            t['username'] = username
            rows.append(t)
        with open('USER_ID.csv', 'w', ) as csvfile:
            fieldnames = ["userId", "username", "completed", "title"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                    quoting=csv.QUOTE_ALL, delimiter=",",
                                    quotechar='"', extrasaction='ignore')
            writer.writerows(rows)
