#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python:top-ten-script:v1.0 (by /u/yourusername)'}
    try:
        resp = requests.get(url,
                            headers=headers,
                            allow_redirects=False,
                            params={'limit': 10})
    except requests.RequestException:
        # Network or other request failure
        print(None)
        return

    # If invalid subreddit, Reddit returns 302 redirect to search results
    if resp.status_code == 302 or resp.status_code == 301:
        print(None)
        return

    if resp.status_code != 200:
        print(None)
        return

    data = resp.json()
    if 'data' not in data or 'children' not in data['data']:
        print(None)
        return

    for post in data['data']['children']:
        title = post['data'].get('title')
        if title:
            print(title)


