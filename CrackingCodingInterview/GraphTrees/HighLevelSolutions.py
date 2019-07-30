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

# 4.8 First Common Ancestor
"""
Problem: Design an algorithm and write code to find the first common ancestor of two nodes in
a binary tree. Avoid storing additional nodes in a data structure. Note: This is not necessarily a binary search tree.

Solution: Pass a parameter that acts as a counter. At the base case check whether the root == one of the nodes 
being searched for if it is then increment the counter. Then after the recursive part where you do 
firstCommonAncestor(root.left, counter) and firstCommonAncestor(root.right, counter) have 

Solution 2: You could look at this as the similar problem 2.7 where given two linked lists find the interection.
So in this case you find both nodes, and then look for the intersection between the two paths.
"""

# 4.9 BST Sequence
"""
Problem: A binary search tree was created by traversing through an array from left to right and inserting
each element. Given a binary search tree with distinct elements, print all possible arrays that could have
led to this tree.

To be continued...
"""

# 4.10 Check Subtree
"""
Problem: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm
to determine if T2 is a subtree of T1. A tree T2 is a subtree of T1 if there exists a node n in T1 such that
the subtree of n is identical to T2. That is if you cut off the tree at node n, the two trees would be identical.

Brute Force Solution: Have one method that does any sort* of traversal through two trees at the same time 
and simply checks that the nodes at that point in the traversal are equal to each other. Then have a driver 
method that visits every node in T1 and plugs node that as the root into one of the trees getting compared in the previous method
and T2 as the other. If the first method returns true then return true from the driver, and do this for every node.

Optimization: Look at the root of T2 and do a search for a node == T2 root in T1, then perform a comparison
of the trees as mentioned in the first method of the brute force solution.

*Note: Cannot use any sort of traversal you want to essentially a DFS where you do: return matchTree(r1.left, r2.left) and
matchTree(r1.right, r2.right) and then in the base case checks see if they are equal (this essentially described above)

Time Complexity: O(n + km) where n is the number of ndoes and k is the number of nodes that equal the root of T2 and m is the number of nodes in T2
even though we most likely would not hit m number of nodes if there are multiple k's because the subtrees will either equal or not equal T2
"""

# 4.11 Random Node
"""
Problem: You are implementing a binary search tree class from scratch which also has a method called
getRandomNode() which returns a random node from the tree. All nodes should be equally likely to be chosen.
Design and implement an algorithm for getRandomNode() and explain how you would implement the rest of the methods.

Solution: To implement this I would replicate how a binary heap is created using an arary and where left of root is
index 2k and right of root is index 2k + 1. Then maintain this list in the tree class. Everytime, an insert or delete
would occur this list would be modified based upon the rules described above. Then to create getRandomNode() I would simply
use randint(1,len(bstList)) to choose a random index in the list and return this value.

Time Complexity: O(1) getRandomNode() but O(log(n)) for deletions and insertions
Space Complexity: O(n)
"""

# 4.12 Paths with Sum
"""
Problem: You are given a binary tree in which each node contains an integer value (which must be positive or negative).
Design an algorithm to count the number of paths that sum to a give value. The path does not need to start or end at the root 
or a leaf, but it must go downwards (only from parent nodes to child nodes).

Solution: Maintain an array that is of size of all the nodes in the tree (if size is not knwon find it)
then perform a DFS traversal where every dfs(root.left) you also add the left node to the array by doing 2k
where k will be an index that you will pass through as a parameter starting as 1, then when going right you index
the array by doing 2k + 1. Once the array is populated, then do the backpack DP solution but instead of only decrementing
by -1 or -2 you decrement by -2k or -2k - 1, and incrementing a counter everytime you find a solution.

Time Complexity: O(n) where n are the total amount of nodes
Space Complexity: O(n)
"""