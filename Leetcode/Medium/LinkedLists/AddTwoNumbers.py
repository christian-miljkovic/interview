"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num_one = 0
        num_two = 0
        
        base_index_one = 1
        base_index_two = 1
        
        curr_one = l1
        curr_two = l2
        
        while curr_one != None:
            num_one += curr_one.val*base_index_one
            base_index_one *= 10
            curr_one = curr_one.next
        
        while curr_two != None:
            num_two += curr_two.val*base_index_two
            base_index_two *= 10
            curr_two = curr_two.next
            
        str_sum = str(num_one+num_two) 
        
        head = ListNode(None)
        curr = head
        
        for i in range(len(str_sum)-1,0,-1):
            curr.val = str_sum[i]
            curr.next = ListNode(None)
            curr = curr.next
        
        curr.val = str_sum[0]
            
        return head