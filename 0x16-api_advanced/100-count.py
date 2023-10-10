#!/usr/bin/python3
""" fetching data from reddit api """

import requests

def count_words(subreddit, word_list):
    """Returns counts of given words found in hot posts of a given subreddit."""
    headers = {'User-agent': 'osajele odegua'}
    posts = requests.get('http://www.reddit.com/r/{}/hot.json'.format(subreddit), headers=headers)

    if posts.status_code == 200:
        posts = posts.json()['data']['children']
        result = {word.lower(): 0 for word in word_list}
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in result:
                    result[word] += 1
        return result
    else:
        return None
