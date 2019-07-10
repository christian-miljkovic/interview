"""
LRUCache cache = LRUCache( 3 /* capacity */ );

cache.put(1, 1) <-
cache.put(2, 2) 
cache.put(3, 3)

1 - 2 - 3

cache.get(1) 

2 - 3 - 1

cache.put(4, 4)

3 - 1 - 4 

cache.put(3, 100)

1 - 4 - 3 

cache.put(5, 5)

4 - 3 - 5


cache.get(9000) -> None

cache.get(4) -> 4

500 elements <- 1 - 3 - 4 -> 500elements
"""

class LRU:
    
    def __init__(self, capacity = 0):
        self.hash_map = dict()
        self.capacity = capacity
        
        self.head = LRUNode()
        self.end = LRUNode()
        
        self.size = 0
        
    #N 2 2 2 2 2 2 - 1 - N
    def addToFront(self, node):
        
        if(node != None):
            node.prev = self.head.prev
            node.next = self.head
            self.head.prev = node
            
            
   # N - 1 - 2 - 3 - 2- N
    remove(2)
    def removeNode(self,node):
        
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
        return node

        
    def get(self, key):
        
        node = self.hash_map[key]
        removed_node = self.removeNode(node)
        self.addToFront(removed_node)
        
        
    def put(self, key, val):
        
        if(key in self.hash_map.keys()):
            node = self.hash_map[key]
            node.data = val
            removed_node = self.removeNode(node)
            self.addToFront(removed_node)
        else:
            node = Node(value)
            self.hash_map[key] = node
            if(self.capacity > self.size):
                self.addToFront(node)
            else:
                self.removeNode(self.end.next)
                self.addToFront(node)
        
        

class LRUNode:
    
    def __init__(self,data=None):
        self.next = None
        self.prev = None
        self.data = data
        


lru = LRU(1000)