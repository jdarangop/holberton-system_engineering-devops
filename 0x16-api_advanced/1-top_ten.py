#!/usr/bin/python3
""" module 0 """
from requests import get


def top_ten(subreddit):
    """ top_ten - Returns the titles of the first 10 hot post
        in a subreddit.
        parameters: subreddit.
        Return: the numeber of subscribers or 0 is not a valid subreddit.
    """
    request = get('https://www.reddit.com/r/{}/top.json?limit=10'
                  .format(subreddit), headers={'User-Agent': 'jdarangop'})

    if request.status_code != 200:
        print(None)
    else:
        list_post = request.json().get('data').get('children')
        for i in list_post:
            print(i.get('data').get('title'))
