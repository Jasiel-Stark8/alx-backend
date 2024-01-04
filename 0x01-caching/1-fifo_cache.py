#!/usr/bin/python3
"""FIFOCache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching.
    Implements the FIFO caching algorithm.
    """
    def __init__(self):
        """Initialize Class"""
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data.
        If the cache exceeds its limit, remove the first item added.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.key_order.append(key)

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.key_order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            return None

    def get(self, key):
        """
        Return the value linked to the key from self.cache_data.
        If key is None or doesn’t exist, return None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
