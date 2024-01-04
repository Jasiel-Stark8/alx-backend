#!/usr/bin/python3
"""LRUCache Module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching.
    Implements the LRU caching algorithm."""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """sumary_line"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.key_order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.key_order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.key_order.append(key)

    def get(self, key):
        """Get cache"""
        if key is not None and key in self.cache_data:
            self.key_order.remove(key)
            self.key_order.append(key)
            return self.cache_data[key]
        return None
