#!/usr/bin/python3
"""_summary_"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.
    This caching system doesn't have a limit.
    """
    def put(self, key, item):
        """
        Assign the item value for the key key in self.cache_data.
        If key or item is None, this method should not do anything.
        """
        if key is not None or key is not None:
            self.cache_data[key] = item

        return self.cache_data

    def get(self, key):
        """
        Return the value linked to the key from self.cache_data.
        If key is None or if the key doesn't exist in self.cache_data, return None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
