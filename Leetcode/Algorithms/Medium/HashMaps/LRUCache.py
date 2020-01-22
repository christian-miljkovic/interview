"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

# Revised solution
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        
        if key in self.cache:
            self.put(key, self.cache[key])
            return self.cache[key]
            
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            del self.cache[key]
        
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value) 



# Efficient use of OrderedDict() class to completely implement

class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        
        if key in self:
            self.move_to_end(key)
        
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# THIS IMPLEMENTATION DOES NOT TAKE DUPLICATE KEYS INTO CONSIDERATION


class LRUCache:

    def __init__(self, capacity: int):
        self.table = dict()
        self.capacity = capacity
        self.queue = collections.deque()
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.table:
            val = self.table[key]
            self.put(key, val)
            return val
        
        return -1
            
        

    def put(self, key: int, value: int) -> None:
        if key not in self.table:
            if self.size == self.capacity:
                remove_key = self.queue.popleft()
                del self.table[remove_key]
                self.size -= 1
            
            self.table[key] = value
            self.size += 1
            self.queue.append(key)
        
        else:
            self.queue.remove(key)
            self.queue.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)