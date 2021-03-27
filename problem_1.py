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
            self.cache.move_to_end(key) # moving key to end of the ordered dictionary before returning value of key
            return self.cache[key]
        else: # cache miss
            return -1

    def set(self, key, value):
        """
        Set the value if the key is not present in the cache
        If cache is at full capacity - oldest item will be removed
        """
        if key is None or value is None:
            print(
"""Please input valid key/value
NOTE: NO KEY/VALUE HAVE BEEN ADDED THE CACHE!\n"""
            )
            return

        if self.num_entries == self.capacity:
            self.cache.popitem(last=False)
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value
            self.cache.move_to_end(key)
            self.num_entries += 1

if __name__ == "__main__":

    # Test Case 1
    print("-----------------------------------------TEST CASE 1-----------------------------------------")

    our_cache = LRU_Cache(5)

    our_cache.set(None, 1)
    our_cache.set(1, None)

    print(our_cache.get(1)) # returns -1 as no key/value pair has been added to cache

    # Test Case 2
    print("-----------------------------------------TEST CASE 2-----------------------------------------")
    our_cache = LRU_Cache(10000)

    # Creating large quantity of key/value pairs
    input_dict = {x : x for x in range(10000)}

    # Inputting the large dictionary into our cache
    for x, y in input_dict.items():
        our_cache.set(x, y)

    print(our_cache.get(0)) # returns 0
    print(our_cache.get(10)) # returns 10
    print(our_cache.get(100)) # returns 100

    our_cache.set(10001, 10001)

    print(our_cache.get(1)) # returns -1 as we have reached maximum capacity for our LRU so 1 is popped to accomodate 10001
    
    # Test Case 3
    print("-----------------------------------------TEST CASE 3-----------------------------------------")
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1)) # returns 1
    print(our_cache.get(2)) # returns 2
    print(our_cache.get(9)) # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(3)) # returns -1 because the cache reached its capacity and 3 was the least recently used entry

