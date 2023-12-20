#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid


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
