#!/usr/bin/python3
"""MRUCache Module"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching.
    Implements the MRU caching algorithm
    """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data.
        If the cache exceeds its limit, remove the least recently used item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.key_order:
                self.key_order.remove(key)
            self.key_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.key_order.pop(-1)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Return the value linked to the key from self.cache_data.
        Update the key as most recently used
        """
        if key is not None and key in self.cache_data:
            self.key_order.remove(key)
            self.key_order.append(key)
            return self.cache_data[key]
        return None
