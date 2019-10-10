"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

"""

"""
Input: listNode start of the LL
Edge Cases:
- None node
- Single node
- Odd number of nodes
- Even number of nodes
- values could be strings or integers

Sub-optimal Solution: hash_table = Counter -> loop through adding to hash_table then loop through hash_table and make sure all but one entry is not odd. If more than one odd then return false else true.

Optimal: Assuming that if at the end of the algorithm a previously instantiated stack is empty == O(1) then ... insert into stack, then as you are doing second iteration pop each element from stack if val != pop_val the return false 


Output: true or false if palindrome

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        
        stack = collections.deque()
        
        curr = head
        while curr:
            stack.appendleft(curr.val)
            curr = curr.next
        
        curr_two = head
        while curr_two:
            pop_val = stack.popleft()
            if pop_val != curr_two.val:
                return False
            curr_two = curr_two.next
            
        return True