#!/usr/bin/python3
"""This script will get the top 10 hot posts for subreddit
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=""):
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

        if hot_list:
            newList = [word for item in hot_list for word in item.split()]
            newList = [s.lower() for s in newList]
            word_list = [w.lower() for w in word_list]
            f_list = []
            for word in word_list:
                occur = newList.count(word)
                if occur > 0:
                    new_dict = {}
                    new_dict['word'] = word
                    new_dict['occur'] = occur
                    f_list.append(new_dict)
            f_list = sorted(f_list, key=lambda k: k['occur'], reverse=True)
            for f in f_list:
                print("{}: {}".format(f.get('word'), f.get('occur')))
    else:
        res = response.json().get('data').get('children')
        t_list = [d.get('data').get('title') for d in res]
        hot_list += t_list
        after = response.json().get('data').get('after')
        count_words(subreddit, word_list, hot_list, after)
        return None
