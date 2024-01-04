#!/usr/bin/python3
"""LIFOCache Module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache Class implements Last-In-First-Out caching strategy"""
    def __init__(self):
        """Initialize Class"""
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data.
        If the cache exceeds its limit, remove the last item added
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.key_order.remove(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discarded_key = self.key_order.pop(-1)
                    del self.cache_data[discarded_key]
                    print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item
            self.key_order.append(key)

    def get(self, key):
        """
        Return the value linked to the key from self.cache_data.
        If key is None or doesn't exist, return None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
