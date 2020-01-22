"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time Complexity: O(m + n)
# Space Complexity: O(1)

class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 and not l2:
            return None
        elif not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1
        
        head = ListNode(None)
        curr = head
        
        while l1 and l2:
            
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
            
        while l1:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
            
        while l2:
            curr.next = l2
            l2 = l2.next
            curr = curr.next
            
        return head.next
        
        



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1 == None and l2 == None:
            return ListNode(None)
        
        new_head = ListNode(None)
        curr_one = l1
        curr_two = l2
        
        if l1.val <= l2.val:
            new_head.val = l1.val
            curr_one = l1.next
        else:
            new_head.val = l2.val
            curr_two = l2.next
            
        curr_head = new_head
        
        while curr_one != None and curr_two != None:
            if curr_one.val <= curr_two.val:
                curr_head.next = ListNode(curr_one.val)
                curr_one = curr_one.next
                curr_head = curr_head.next
            else:
                curr_head.next = ListNode(curr_two.val)
                curr_two = curr_two.next
                curr_head = curr_head.next
                
        if curr_one != None:
            while curr_one != None:
                curr_head.next = ListNode(curr_one.val)
                curr_one = curr_one.next
                curr_head = curr_head.next
                
        if curr_two != None:
            while curr_two != None:
                curr_head.next = ListNode(curr_two.val)
                curr_two = curr_two.next
                curr_head = curr_head.next
                
        return new_head