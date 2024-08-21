#!/usr/bin/python3
"""A LFU caching system with limit"""
from typing import Any

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Simple class representation of a LFU caching system"""
    def __init__(self) -> None:
        """Initialize an instance with parent class attributed"""
        self.lfu = {}
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
                val = sorted([v for v in self.lfu.values()])[0]
                for k in self.lfu.keys():
                    if self.lfu.get(k) == val:
                        key_to_del = k
                        break
                print(self.lfu)
                del self.cache_data[key_to_del]
                del self.lfu[key_to_del]
                print("DISCARD: {}".format(key_to_del))
            self.cache_data[key] = item
            if self.lfu.get(key):
                self.lfu[key] = self.lfu[key] + 1
            else:
                self.lfu[key] = 0

    def get(self, key: Any) -> Any:
        """Gets an item from the cache dict
        Params:
            key - key of item to get
        Return:
            Item or none
        """
        item = self.cache_data.get(key)
        if item:
            self.lfu[key] = self.lfu[key] + 1
        return item
