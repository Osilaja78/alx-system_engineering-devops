#!/usr/bin/python3
"""Module for advanced task"""


import requests
import re
from collections import Counter


def count_words(subreddit, word_list, results=None, after=None):
    """
    Queries the reddit API and parses the title
    of all hot articles, and prints a sorted
    count of given keywords.
    """

    if results is None:
        results = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f'&after={after}'

    headers = {"User-Agent": "MyALXRedditBot/1.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"].lower()
            for keyword in word_list:
                if re.search(rf'\b{re.escape(keyword)}\b', title):
                    results[keyword] += 1

        after = data["data"]["after"]
        if after:
            return count_words(subreddit, word_list, results, after)
        else:
            print_results(results)
    else:
        return


def print_results(results):
    """Prints the sorted results accordingly"""

    sorted_results = sorted(
        results.items(),
        key=lambda x: (-x[1], x[0])
    )

    for keyword, count in sorted_results:
        print(f"{keyword}: {count}")
