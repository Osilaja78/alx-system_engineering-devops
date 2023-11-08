#!/usr/bin/python3
"""Top 10 rddit posts"""


import requests


def top_ten(subreddit):
    """
    Queries the reddit API and gets the top
    10 reddit posts.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {"User-Agent": "MyALXRedditBot/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
