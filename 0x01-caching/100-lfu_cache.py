#!/usr/bin/env python3
"""LFUCache Module"""
from base_caching import BaseCaching
from collections import defaultdict

class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching.
    Implements the LFU caching algorithm
    """
    def __init__(self):
        """Initialize Class"""
        super().__init__()
        self.key_access_frequency = defaultdict(int)
        self.key_order = []

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data.
        If the cache exceeds its limit, remove the least frequently used item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if key in self.key_access_frequency:
            self.key_order.remove(key)
        else:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_frequent = min(self.key_access_frequency)
                self.key_order.remove(least_frequent)
                del self.cache_data[least_frequent]
                del self.key_access_frequency[least_frequent]
                print(f"DISCARD: {least_frequent}")

        self.key_access_frequency[key] += 1
        self.key_order.append(key)

    def get(self, key):
        """sumary"""
        if key is not None and key in self.cache_data:
            self.key_order.remove(key)
            self.key_order.append(key)
            self.key_access_frequency[key]  += 1
            return self.cache_data[key]
        return None
