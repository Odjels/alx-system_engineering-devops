#!/usr/bin/python3
""" retrieve titles of posts """

import requests


def top_ten(subreddit):
    """ function to retrieve post titles 10 in number """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-agent": "osajele odegua"}

    posts = requests.get(url, headers=headers, allow_redirects=False)

    if posts.status_code == 200:
        for post in posts.json()['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
