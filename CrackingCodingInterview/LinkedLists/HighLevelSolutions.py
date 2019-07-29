"""
Chapter 2 - Linked Lists 
These are high level solutions that I created for the rest of the practice problems in this chapter
"""

# 2.4 Partition
"""
Problem: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. 

Example
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

Solution: Initialize 3 pointers lessThanHead, partitionHead, greaterThanHead to None then as you loop through the original
singly linked list add the nodes based upon where they fall within the above "categories" and point the new head to those nodes
If partition value is found multiple times add it to the same pointer.
At the end of the loop if partitionHead == None return None otherwise connect the seperate linked lists (lessThan linked list
will need to have a pointer to the head and tail so that you can connect and then return the head as the beginning of entire list)

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(n) since you are creating a new linked list

"""

# 2.5 Sum Lists
"""
Problem: You have two numbers represented by two linked list, where each node contains a single digit. The digits
are stored in reverse order such that 1's digit is at the head of the list. Write a function that adds the two numbers
and returns the sum as a linked list.

Example
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2) is 617 + 295
Output: 2 -> 1 -> 9 

Solution: Store a total variable and multipler variable which starts at 1 and as you loop 
through each linked list do total += node.data * multipler and then multipler *= 10. If it is a single list 
and the plus data node indicates a new number than reset mutlipler equal to 1. Once you are done looping through a list
then you will divide the multipler by 10 so you know the ^10 aka how many times to divide. Then while multipler != 0 you do
total // multipler -> digit to add. Then total = total % mutipler then multipler /= 10.  

Time Complexity: O(n) where n is the length of the longest list 
Space Complexity: O(n) since we are creating a list of the same size

Follow up: We need to be careful if we end up summing two digits together that end up with a digit that has a longer length.
To avoid this we could not prevent the divide by 10 of the multipler by checking if total//multipler > 0. If it is then we keep it,
otherwise divide by 10. Futhermore, we also need two multipler variables because if adding 999 + 1 and the multipler ends up only taking
into consideration the 1 then it will be much lower than what we need. So maintain two, see which is largest, then do the check on the total.
"""

# 2.6 Palindrome
"""
Problem: Implement a function to check if a linked list is a palindrome.

Solution: Loop through the linked list and add each data point into a stack and list. Once done with looping
through the linked list, use a loop until the end of the list and do a pop() on the stack and compare list[i].
If the two values are not equal return False, otherwise once loop terminates return True.

Time Complexity: O(n) where is the number of nodes
Space Complexity: O(n^2) since we are holding a stack and list of size n

"""

# 2.7 Intersection
"""
Problem: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting 
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second linkde list
then they are interesting.

Solution:

"""