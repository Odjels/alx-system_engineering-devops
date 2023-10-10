#!/usr/bin/python3
""" fetches number of subscribers from reddit api """

import requests


def number_of_subscribers(subreddit):
    """ This function fetches the number of subscribers """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-agent": "Osajele Odegua"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return (data['data']['subscribers'])
    else:
        return 0
