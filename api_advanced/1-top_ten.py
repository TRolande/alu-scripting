#!/usr/bin/python3
"""
Module to fetch and print the titles of the top 10 hot posts
for a given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """Print titles of the top 10 hot posts of a subreddit, or None on failure."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Python:top_ten_script:v1.0 (by /u/yourusername)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
    except requests.RequestException:
        print(None)
        return

    # Reject redirects (invalid subreddit often returns 301/302)
    if response.status_code in (301, 302):
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return

    if not posts:
        print(None)
        return

    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)

