#!/usr/bin/python3
"""A caching system with limit"""
from typing import Any

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Simple class representation of a caching system"""
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
                discarded_key = [i for i in self.cache_data.keys()][0]
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """Gets an item from the cache dict
        Params:
            key - key of item to get
        Return:
            Item or none
        """
        return self.cache_data.get(key)
