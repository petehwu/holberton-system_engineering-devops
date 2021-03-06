#!/usr/bin/python3
"""This script will get the top 10 hot posts for subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """This function gets the top 10 hot posts for subreddit
    """
    headers = {'User-Agent': 'ubuntu:test.petehwu:v0.0.1 (by/u/petehwu)'}
    uri = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    parameters = {"after": after}
    if (after == ""):
        response = requests.get(uri, allow_redirects=False, headers=headers)
    else:
        response = requests.get(uri, allow_redirects=False,
                                headers=headers, params=parameters)
    if response.status_code in [404, 302] or after is None:
        if not hot_list:
            return None
        else:
            return hot_list
    else:
        res = response.json().get('data').get('children')
        t_list = [d.get('data').get('title') for d in res]
        hot_list += t_list
        after = response.json().get('data').get('after')
        return(recurse(subreddit, hot_list, after))
