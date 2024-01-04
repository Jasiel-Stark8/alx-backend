#!/usr/bin/python3
"""MRUCache Module"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching.
    Implements the MRU caching algorithm.
    """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.key_order = []  # List to keep track of the keys' usage order

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data.
        If the cache exceeds its limit, remove the most recently used item.
        """
        if key is not None and item is not None:
            # Update the cache and key order
            self.cache_data[key] = item
            if key in self.key_order:
                # Remove the old key position if it's already in the cache
                self.key_order.remove(key)
            self.key_order.append(key)  # Append key as the most recently used

            # Verify the cache limit and remove the most recently used item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the last key added (MRU)
                discarded_key = self.key_order.pop(-1)
                del self.cache_data[discarded_key]  # Remove from cache_data
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Return the value linked to the key from self.cache_data.
        Update the key as most recently used.
        """
        if key is not None and key in self.cache_data:
            # Update key as most recently used
            self.key_order.remove(key)
            self.key_order.append(key)
            return self.cache_data[key]
        return None
