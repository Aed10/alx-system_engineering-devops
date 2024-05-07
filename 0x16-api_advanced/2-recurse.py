#!/usr/bin/python3
"""
Module for recurse function
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit. If no results are
    found for the given subreddit, the function should return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Edg/124.0.0.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    children = data.get("children")
    for child in children:
        hot_list.append(child.get("data").get("title"))
    after = data.get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list)
