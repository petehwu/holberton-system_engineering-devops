#!/usr/bin/python3
"""This script will get the top 10 hot posts for subreddit
"""
import requests


def top_ten(subreddit):
    """This function gets the top 10 hot posts for subreddit
    """
    headers = {'User-Agent': 'ubuntu:test.petehwu:v0.0.1 (by/u/petehwu)'}
    parameters = {'limit': 10}
    uri = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(uri, allow_redirects=False, headers=headers,
                            params=parameters)
    if response.status_code == 404:
        print("None")
    else:
        res = response.json().get('data').get('children')
        print(*[d.get('data').get('title') for d in res], sep='\n')
