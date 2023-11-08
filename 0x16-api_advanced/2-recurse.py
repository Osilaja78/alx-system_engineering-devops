#!/usr/bin/python3
"""Retrieve hot articles for a subreddit"""


import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Queries the reddit API and gets the
    hot articles for a subreddit.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f'&after={after}'

    headers = {"User-Agent": "MyALXRedditBot/1.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            hot_list.append(post["data"]["title"])

        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
