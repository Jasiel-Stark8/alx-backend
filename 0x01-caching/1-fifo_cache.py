#!/usr/bin/python3
"""_summary_"""
from typing import Union
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class
    """
    def __init__(self):
        """Sumary_line"""
        super().__init__()
        self.key_order = []

    def put(self, key: Union[str, int], item: Union[str, int]) -> None:
        """sumary_line"""
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.key_order.append(key)

            self.cache_data[key] = item

            if len(self.cache_data[key]) > BaseCaching.MAX_ITEMS:
                discarded_key = self.key_order.pop(key)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
        return None

    def get(self, key):
        """sumary_line"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
