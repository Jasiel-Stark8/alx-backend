#!/usr/bin/python3
""" BasicCache module. """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching.
    This caching system doesn’t have a limit. """

    def put(self, key, item):
        """ Assign the item value for the key key in self.cache_data.
        If key or item is None, this method should not do anything. """
        if key is not None and item is not None:
            self.cache_data[key] = item  # Properly assign the item to the key in cache_data

    def get(self, key):
        """ Return the value linked to the key from self.cache_data.
        If key is None or if the key doesn’t exist in self.cache_data, return None. """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]  # Return the value associated with the given key
        return None  # Return None if key is not found or is None
