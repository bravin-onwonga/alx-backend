#!/usr/bin/python3
"""A LRU caching system with limit"""
from typing import Any

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Simple class representation of a LRU caching system"""
    def __init__(self) -> None:
        """Initialize an instance with parent class attributed"""
        self.lru = {}
        self.access = 0
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
                val = sorted([v for v in self.lru.values()])[0]
                for k in self.lru.keys():
                    if self.lru.get(k) == val:
                        key_to_del = k
                del self.cache_data[key_to_del]
                del self.lru[key_to_del]
                print("DISCARD: {}".format(key_to_del))
            self.cache_data[key] = item
            self.access += 1
            self.lru[key] = self.access

    def get(self, key: Any) -> Any:
        """Gets an item from the cache dict
        Params:
            key - key of item to get
        Return:
            Item or none
        """
        item = self.cache_data.get(key)
        if item:
            self.access += 1
            self.lru[key] = self.access
        return item
