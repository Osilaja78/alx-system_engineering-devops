#!/usr/bin/python3
"""Subreddit subscribers"""


import requests


def number_of_subscribers(subreddit):
    """
    Queries the reddit API and gets number
    of subreddit subscribers
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "MyAlxRedditBot/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subs = data["data"]["subscribers"]
        return subs
    else:
        return 0
