#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
from functools import wraps
import redis
import requests
cache = redis.Redis()


def page_count(method):
    """
    get page count
    """

    @wraps(method)
    def wrapper(url):
        """
        the wrapper
        """
        cache_key = "cached:" + url
        cache_data = cache.get(cache_key)
        htmlpage = method(url)
        if cache_data is None:
            cache.set(cache_key, htmlpage)

        count_key = "count:" + url
        cache.incr(count_key)
        cache.expire(cache_key, 10)
        return htmlpage
    return wrapper


@page_count
def get_page(url: str) -> str:
    """
    get web page content
    """
    page = requests.get(url)
    return page.text
