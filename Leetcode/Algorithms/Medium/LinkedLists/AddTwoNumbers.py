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

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l1_val = list_to_number(l1)
        l2_val = list_to_number(l2)
        
        total_str = str(l1_val + l2_val)[::-1]
        head = l1 if l1_val >= l2_val else l2
        
        return number_to_list(total_str, head)
    

def number_to_list(str_number, head):
    
    new_head = head
    curr = head
    
    # Overwrite 
    for index, char in enumerate(str_number):
        curr.val = int(char)
        if not curr.next and index < len(str_number) - 1:
            curr.next = ListNode(None)
        curr = curr.next

    return new_head
        
def list_to_number(head):
    
    total = 0
    base = 1
    curr = head
    
    while curr:
        total += curr.val * base
        base *= 10
        curr = curr.next
        
    return total


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
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