'''

LRU Cache

Keeps track of how recently data is used

when there is no space for new data, remove the item that hasn't been
accessed for the longest time, and store the new item

'''

from collections import deque

class lru_cache:
    def __init__(self,capacity: int):
        self.capacity = capacity

        # Dictionary to store key-value pairs
        self.cache = {}

        # Deque to maintain order of keys
        self.order = deque()

    def get(self,key: int):
        if key in self.cache:

            # move the accessed key to the front
            self.order.remove(key)
            self.order.appendleft(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int):
        if key in self.cache:

            # Update the value and move the key to the front
            self.cache[key] = value
            self.order.remove(key)
            self.order.appendleft(key)
        else:
            if len(self.cache) >= self.capacity:
                lru_key = self.order.pop()
                del self.cache[lru_key]

            self.cache[key] = value
            self.order.appendleft(key)