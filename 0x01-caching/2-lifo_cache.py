#!/usr/bin/python3
"""LIFOCache Module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache Class"""
    def __init__(self):
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.key_order.remove(key)
            else:
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    discarded_key = self.key_order.pop(-1)
                    print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item
            self.key_order.append(key)

        

    def get(self, key):
        """sumary_line"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
