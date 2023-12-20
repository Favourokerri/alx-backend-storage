#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union


class Cache:
    """ cache class """
    def __init__(self):
        """ instance of redis """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            store method with agument data
            sets the value in our redis and
            return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn=None):
        """ 
            method that gets items from 
            redis
        """
        if fn is None:
            return self._redis.get(key)
        else:
            converted_value = fn(self._redis.get(key))
            return converted_value

    def get_str(self, key: str) -> str:
        """
            automatically parametrize Cache.get
            with str value
        """
        return self._redis.get(key).decode('utf-8')

    def get_int(self, key: int) -> int:
        """
            automatically parametrize Cache.get
            with int value
        """
        value = self._redis.get(key)
        return int(value)
