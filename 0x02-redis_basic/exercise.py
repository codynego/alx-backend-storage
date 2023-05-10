#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
from uuid import uuid4
from typing import List, Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, int, bytes, float]:
        """
        A method gets a value from redis
        Args:
            key (str): the key
            fn (Optional[Callable]): a callable
        Return:
            returns the value
        """
        value: str = self._redis.get(key)
        if fn:
            value = fn(value)
        return value
