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
    word_list = [word.lower() for word in word_list]
    word_list = set(word_list)
    if not hot_list:
        hot_list = [{'word': w, 'occur': 0} for w in word_list]
    if response.status_code != 200 or after is None:
        hot_list = [dd for dd in hot_list if dd.get('occur') > 0]
        if not hot_list:
            return word_list
        else:
            hot_list = sorted(hot_list, key=lambda k: k['occur'], reverse=True)
            for h in hot_list:
                print("{}: {}".format(h.get('word'), h.get('occur')))
            # hot_list2 = [(h.get('word'), h.get('occur')) for h in hot_list]
            # return hot_list2
            return word_list
    else:
        res = response.json().get('data').get('children')
        t_list = [d.get('data').get('title') for d in res]
        t_list = [word.lower() for item in t_list for word in item.split(" ")]
        t_list.sort()
        for wd in hot_list:
            wd['occur'] = wd.get('occur') +\
                          t_list.count(wd.get('word').lower())
        """
        print ("++++++++++++++++++++++++++++")
        print (t_list)
        for h in hot_list:
            print("{}: {}".format(h.get('word'), h.get('occur')))
        print("after {}".format(after))
        print("+++++++++++++++++++++++++++++")
        """
        after = response.json().get('data').get('after')
        return(count_words(subreddit, word_list, hot_list, after))
