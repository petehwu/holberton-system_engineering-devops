#!/usr/bin/python3
"""This script will get the number of subscribers for subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """This function gets the number of subscribers for subreddit
    """
    user_agent = {'User-Agent': 'ubuntu:test.petehwu:v0.0.1 (by/u/petehwu)'}
    uri = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(uri, allow_redirects=False, headers=user_agent)
    if response.status_code in [404, 302]:
        return 0
    else:
        res = response.json()
        return (res.get('data').get('subscribers'))
