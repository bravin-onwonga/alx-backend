#!/usr/bin/python3
"""A LIFO caching system with limit"""
from typing import Any

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Simple class representation of a LIFO caching system"""
    def __init__(self) -> None:
        """Initialize an instance with parent class attributed"""
        super().__init__()

    def put(self, key: Any, item: Any) -> None:
        """Adds an item to the cache dict
        Params:
            key - key of item to get
            item - item to add
        """
        if key and item:
            dct_len = len(self.cache_data)
            if dct_len == BaseCaching.MAX_ITEMS and key not in self.cache_data:
                discarded_pair = self.cache_data.popitem()
                print("DISCARD: {}".format(discarded_pair[0]))
            self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """Gets an item from the cache dict
        Params:
            key - key of item to get
        Return:
            Item or none
        """
        return self.cache_data.get(key)
