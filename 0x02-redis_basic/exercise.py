#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
from uuid import uuid4
from typing import List, Union


class Cache:
    """
    A cache class
    """
    def __init__(self):
        """
        Initializing the cache instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        a method saves or set a data to redis
        Args:
            data (Union[str, bytes, int, float]) - the data to set
        Return:
            returns the key (str)
        """
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key
