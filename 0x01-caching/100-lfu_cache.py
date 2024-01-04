#!/usr/bin/env python3
"""LFUCache Module"""
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """LFUCache class that inherits from BaseCaching.
    Implements the LFU caching algorithm."""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.key_access_frequency = defaultdict(int)  # To track access frequency of keys
        self.key_order = []  # To track the order of key insertions for tie-breaking

    def put(self, key, item):
        """Assign the item value for the key in self.cache_data.
        If the cache exceeds its limit, remove the least frequently used item."""
        if key is not None and item is not None:
            # Update the cache
            self.cache_data[key] = item

            # Update the frequency
            if key in self.key_access_frequency:
                self.key_order.remove(key)
            else:
                # Verify the cache limit and remove the least frequently used item
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    # Find the least frequently used key
                    least_frequent = min(self.key_access_frequency, key=lambda k: (self.key_access_frequency[k], self.key_order.index(k)))
                    self.key_order.remove(least_frequent)
                    del self.cache_data[least_frequent]
                    del self.key_access_frequency[least_frequent]
                    print(f"DISCARD: {least_frequent}")

            # Record the key as most recently used
            self.key_access_frequency[key] += 1
            self.key_order.append(key)

    def get(self, key):
        """Return the value linked to the key from self.cache_data.
        Update the key's access frequency."""
        if key is not None and key in self.cache_data:
            # Update frequency and order
            self.key_order.remove(key)
            self.key_order.append(key)
            self.key_access_frequency[key] += 1
            return self.cache_data[key]
        return None
