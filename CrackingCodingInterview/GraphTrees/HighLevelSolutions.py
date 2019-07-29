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

# 4.5 Validate BST
"""
Problem: Implement a function to check if a binary tree is a binary search tree

Solution: While performing a DFS check that if a node has a left child that the data is less than or 
equal to the parent and if there is a right child that the data is greater than it.

Time Complexity: O(n) where n is the number of nodes

Fix: We will need to pass down a min and max value (can be in the form of an object) because
a proper BST has all nodes in left subtree less than the parent node, and all nodes in right tree have to be
greater than. If we assumed what we did in the initial solution you could have for example an 
instance where the second level on the left subtree has a greater value than the first root node. That is why
as we traverse down we just need to pass a min, max like this -> validateBST(root.left, min, root.data)
and validateBST(root.right, root.data, max) then if the current node being inspected doesn't fall in the
range of min and max then return false.
"""

# 4.6 Successor
"""
Problem: Write an algorithm to find the "next" node i.e. in-order successor of a given node in 
a binary search tree. You may assume that each node has a link to its parent.

Solution: Pass an empty list through as a parameter, and then as you perform an in-order traversal
if you hit the node that you are looking for append it to the list. Another base case should be then 
if the stack size == 1 then return the next node that gets traversed. This should be the in-order successor.

Update: We could just use a flag instead of a list to indicate we have the node before the successor and therefore
pass a boolean that we set once we find the first node to indicate that the next is the successor. 

Time Complexity: O(n)
"""

# 4.7 Build Order
"""
Problem: You are given a list of projects and a list of dependencies (list of pairs where second project
is dependent on the first project). All projects dependencies must be built before the project is. 
Find a build order that will allow the projects to be built. If there is no valid order, return an error.

Example
Input: projects a, b, c, d, e, f
       dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c

Solution: Create a graph where each node has a parent edge and then a list of children by adding
looping through the projects list and creating a node for each project as well as 
incrementing the size of graph per node. Then loop through the  dependencies and if there are any 
"children" of that project and also see if it has a parent. Once the graph is constructed loop through the 
graph and find all nodes with no parent, then perform a pre-order traversal (while adding nodes to a list). 
If len(list) != graph_size return error, otherwise ', '.join(list) which should be the output we for depedencies.

Optimize: Perform a topological sort once you have the graph created, the above solution didn't take into account
a single project having multiple dependencies. 
"""
