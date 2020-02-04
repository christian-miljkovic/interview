"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:

You must return the copy of the given head as a reference to the cloned list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
# Refactored 

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return None
        
        node_map = dict()
        new_head = copy_random_node(head, node_map)
        curr = new_head
       
        
        while head:
            
            curr.next = copy_random_node(head.next, node_map)
            curr.random = copy_random_node(head.random, node_map)
            
            curr = curr.next
            head = head.next

        return new_head
        
def copy_random_node(curr_node, node_map):
    
    if not curr_node:
        return None
    
    if curr_node not in node_map:
        random_node = Node(curr_node.val)
        node_map[curr_node] = random_node
    
    return node_map[curr_node]



# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return head
        
        is_visited = dict()
        copy_head = Node(head.val, None, None)
        is_visited[head] = copy_head
        curr = copy_head
        
        while head:
            
            curr.next = copy_node(head.next, is_visited)
            curr.random = copy_node(head.random, is_visited)            
            curr = curr.next
            head = head.next
            
        return copy_head
        
        
        
        
def copy_node(node, is_visited):
    
    if node:
        if node in is_visited:
            return is_visited[node]
        else:
            new_node = Node(node.val, None, None)
            is_visited[node] = new_node
            return new_node