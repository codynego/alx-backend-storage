#!/usr/bin/env python3
""" Main file """

from exercise import Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:input".format(Cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:output".format(Cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))
