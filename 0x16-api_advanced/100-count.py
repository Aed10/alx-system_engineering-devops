#!/usr/bin/python3
"""
Module for count_words function
"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Queries the Reddit API, parses the title of all hot articles, and prints
    a sorted count of given keywords.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Edg/124.0.0.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    children = data.get("children")
    for child in children:
        title = child.get("data").get("title")
        for word in word_list:
            if word.lower() not in word_count:
                word_count[word.lower()] = 0
            word_count[word.lower()] += (
                title.lower().split().count(word.lower())
            )
    after = data.get("after")
    if after is None:
        for key, value in sorted(
            word_count.items(), key=lambda x: x[1], reverse=True
        ):
            if value != 0:
                print(f"{key}: {value}")
        return
    return count_words(subreddit, word_list, word_count, after)
