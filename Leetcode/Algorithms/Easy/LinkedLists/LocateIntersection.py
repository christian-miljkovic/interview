"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

"""
Input: two heads of type listNode
Edge Cases:
- No intersection
- multiple intersections
- one of the heads is == None
- Assumption no cycle 

Output: Reference to the node that is the intersection, or null if there is none

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time Complexity: O(n+m) where n is size of headA and m size of headB
# Space Complexity: O(1)

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        size_a, size_b = 0,0
        curr_a = headA
        curr_b = headB
        
        while curr_a:            
            size_a += 1
            curr_a = curr_a.next
            
        while curr_b:
            size_b += 1
            curr_b = curr_b.next
            
        wait_a, wait_b = 0,0
        
        if size_a > size_b:
            wait_b = size_a - size_b
        else:
            wait_a = size_b - size_a
            
        curr_a = headA
        curr_b = headB
        
        while curr_a and curr_b:
            
            if curr_a == curr_b:
                return curr_a
            
            if wait_a <= 0:
                curr_a = curr_a.next
            
            if wait_b <= 0:
                curr_b = curr_b.next

            wait_a -= 1
            wait_b -= 1
        
        return None
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        