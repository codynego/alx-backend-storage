#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
from uuid import uuid4
from typing import List, Union, Callable, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    """
    decorator to store the history of inputs
    and outputs for a particular function
    """
    name_input = method.__qualname__ + ":inputs"
    name_output = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        a wrapper
        """
        inputs = str(args)
        self._redis.rpush(name_input, inputs)
        outputs = str(method(self, *args, **kwargs))
        self._redis.rpush(name_output, outputs)
        return outputs
    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    a method that counts how many times methods
    of the Cache class are called.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        a wrapper
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


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

    @call_history
    @count_calls
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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, int, bytes, float]:
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

    def get_str(self, key: str) -> str:
        """
        get the string value from redis
        Args:
            key (str): the key
        """

        value = self._redis.get(key)
        return str(value.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        get the integer value from redis
        Args:
            key (str): the key
        Return:
            return the int of value
        """
        value = self._redis.get(key)
        return int(value.decode("utf-8"))
