#!/usr/bin/python3
"""
Module for top_ten function
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Edg/124.0.0.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data")
    children = data.get("children")
    for child in children[:10]:
        print(child.get("data").get("title"))
