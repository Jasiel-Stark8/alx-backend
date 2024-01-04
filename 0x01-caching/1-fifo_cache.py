#!/usr/bin/python3
""" FIFOCache module. """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching.
    Implements the FIFO caching algorithm. """

    def __init__(self):
        """ Initialize the class. """
        super().__init__()
        self.key_order = []  # List to keep track of the order keys were added

    def put(self, key, item):
        """ Assign the item value for the key in self.cache_data.
        If the cache exceeds its limit, remove the first item added. """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.key_order.append(key)  # Track key order

            self.cache_data[key] = item  # Add or update the key-value pair

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the first item added (FIFO)
                discarded_key = self.key_order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ Return the value linked to the key from self.cache_data.
        If key is None or doesn’t exist, return None. """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None