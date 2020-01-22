"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

"""
Input: list of nodes
Edge Cases:
- Empty list
- Even/Odd list sizes 

Assumption:
- These are already pre-sorted

Idea 1: Write every node into an array then sort the array then re-create a single list

Idea 2: Until the array is empty just continuously chop off the first element of the certain linked list and add it to a new list -> this should gives us Time Complexity: O(nm) where n is the length of the longest LL and m is size of array and Space Complexity: O(nm)

Output: one list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    
        lists = [x for x in lists if x is not None]
        
        new_head = ListNode(None)
        curr = new_head
        
        while lists:
            min_index = find_min_node(lists)
            min_node = lists[min_index]
            
            curr.next = ListNode(min_node.val)
            curr = curr.next
            
            min_node = min_node.next            
            if not min_node:
                lists.pop(min_index)
            else:
                lists[min_index] = min_node
            
        
        return new_head.next

def find_min_node(lists):
    
    min_val = lists[0].val
    index = 0
    
    for i in range(0,len(lists)):
        if lists[i].val < min_val:
            index = i
            min_val = lists[i].val
    
    return index
    
    
    