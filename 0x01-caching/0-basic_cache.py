#!/usr/bin/python3
"""A caching system"""
from typing import Any

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
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
            self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """Gets an item from the cache dict
        Params:
            key - key of item to get
        Return:
            Item or none
        """
        return self.cache_data.get(key)
