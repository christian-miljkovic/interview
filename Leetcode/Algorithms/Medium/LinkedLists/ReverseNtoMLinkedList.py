"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

"""





# Invalid solution attempt

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if head:
            
            if m == n:
                return head
            
            count = m
            old_head = head
            curr = head
            
            while count > 1:
                curr = curr.next
                count -= 1
            
            tail, new_head, new_curr = reverse_list(curr, n - m)
            print(tail.val, new_head.val, new_curr.val)
            if old_head.val != tail.val:
                old_head.next = new_head
                tail.next = new_curr
                return old_head
            else:
                tail.next = new_curr
                return new_head

            
            
        
def reverse_list(head, stop_count):
    
    tail = head
    prev = head
    curr = head.next
    
    while stop_count and curr:
        temp = curr.next
        curr.next = prev
        
        prev = curr
        curr = temp
        stop_count -= 1
    
    return tail, prev, curr