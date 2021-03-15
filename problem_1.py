from collections import OrderedDict
class LRU_Cache:
    def __init__(self, capacity):
        """ Initialize class variables """
        # utilizing ordered dictionary in order to access values using key at constant time O(1) as well as have a sorted data structure to consider for the LRU component
        self.cache = OrderedDict()
        self.capacity = capacity
        self.num_entries = 0

    def get(self, key):
        """ Retrieve item from provided key. Returns -1 if nonexistent """
        if key in self.cache.keys(): # cache hit
            # moving key to end of the ordered dictionary before returning value of key
            self.cache.move_to_end(key)
            return self.cache[key]
        else: # cache miss
            # return -1 if key is not found in cache
            return -1

    def set(self, key, value):
        """
        Set the value if the key is not present in the cache
        If cache is at full capacity - oldest item will be removed
        """
        if self.num_entries == self.capacity:
            # pop first item in dictionary which in this case is the least recently used key/value
            self.cache.popitem(last=False)
            # accessing value by utilizing key to search the dictionary in constant time O(1)
            self.cache[key] = value
            # key is moved to the end of the dictionary as it has recently been accessed
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value
            self.cache.move_to_end(key)
            self.num_entries += 1

if __name__ == "__main__":

    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    our_cache.get(1) # returns 1
    our_cache.get(2) # returns 2
    our_cache.get(9) # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    our_cache.get(3) # returns -1 because the cache reached its capacity and 3 was the least recently used entry

