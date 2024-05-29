#!/usr/bin/python3
"""
LRU Caching Module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''
    LRUCache class
    __init__(): Initializes the LRUCache object.
    put: Adds an item to the cache.
    get: Retrieves an item from the cache based on the key.
    '''

    def __init__(self):
        """
        Initialize the LRUCache object.
        """
        super().__init__()
        self.access_order = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the item and move key to end
                self.access_order.pop(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least recently used item (LRU)
                lru_key = next(iter(self.access_order))
                del self.access_order[lru_key]
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.access_order[key] = None
            # Move the key to the end to mark it as recently used
            self.access_order.move_to_end(key)

    def get(self, key):
        """
        Retrieve an item from the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        
        # Move the accessed key to the end to mark it as recently used
        self.access_order.move_to_end(key)
        return self.cache_data[key]

    def print_cache(self):
        """
        Print the current state of the cache.
        """
        print("Current cache:")
        for key in self.cache_data:
            print(f"{key}: {self.cache_data[key]}")
