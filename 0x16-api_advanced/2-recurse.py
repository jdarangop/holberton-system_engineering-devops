#!/usr/bin/python3
""" module 2 """
from requests import get


def recurse(subreddit, hot_list=[], page=None):
    """ top_ten - Returns the titles of the first 10 hot post
        in a subreddit.
        parameters: subreddit.
        Return: the numeber of subscribers or 0 is not a valid subreddit.
    """

    if page is None:
        request = get('https://www.reddit.com/r/{}/hot.json'
                      .format(subreddit), headers={'User-Agent': 'jdarangop'},
                      allow_redirects=False)
    else:
        request = get('https://www.reddit.com/r/{}/hot.json?after={}'
                      .format(subreddit, page),
                      headers={'User-Agent': 'jdarangop'},
                      allow_redirects=False)

    if request.status_code != 200:
        return None
    else:
        after = request.json().get('data').get('after')
        list_post = request.json().get('data').get('children')
        for i in list_post:
            hot_list.append((i.get('data').get('title')))
        if after:
            return(recurse(subreddit, hot_list, after))
        else:
            return hot_list
