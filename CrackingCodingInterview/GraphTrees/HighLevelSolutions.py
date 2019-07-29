"""
Chapter 4 - Graphs and Trees
These are high level solutions that I created for the rest of the practice problems in this chapter
"""

# 4.4 Check Balanced
"""
Problem: Implement a function to check if a binary tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.

Solution: Use a simple object could even be a list of size 2 with two zero's inside to indicate the level 
of the left and right subtree. Then like in DP problems where you do something like total = 1 + recurse()
Do the same but instead have obj[0] += 1 + checkBalanced(root.left, obj) and the same for the right node.
Then at the end of the recursive method check if obj[0] == obj[1] or the -1 case for each side and if so then we know 
the tree is balanced. Otherwise, return false.

See CheckBalanced for complete solution.
"""
