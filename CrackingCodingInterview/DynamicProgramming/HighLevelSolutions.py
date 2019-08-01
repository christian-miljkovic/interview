"""
Chapter 8 - Dynamic Programming
These are high level solutions that I created for the rest of the practice problems in this chapter
"""

# 8.4 Power Set
"""
Problem: Write a method to return all subsets of a set

Solution: See PowerSet.py file
"""

# 8.5 Recursive Multiply
"""
Problem: Write a recursive function to multiply two positive integers without using the * operator.
You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations. 

Solution: Have two parameters a,b where we are trying to get a*b. Base case is when b == 1 return a
otherwise do a += multiply(a,b), then b-= 1. Then recursve and pass the new a and b. See RecusriveMultiply.py for code.

Optimization: If you add a up b/2 times then you can take the sum of that and add it together to get the proper amount 
instead of adding a up b times.  
"""

# 8.6 Towers of Hanoi
"""
Problem: Three towers and N disks of different sizes which can slide onto any tower. Following constraints:
1. Only one disk can be moved at a time 2. A disk is slid off the top of one tower onto another tower
3. A disk cannot be placed on top of a smaller disk

Solution: if n > 0 then move n - 1 disks to the buffer, then move the top of original stack (which should be the last disk)
to the target stack. Move n - 1 disks to target stack. The recusrive method signature should look like:
moveDisks(n, destination, buffer). If we have tower A,B,C then the first recursive call will be moveDisks(n-1, C, B)
followed by moveTopDisk(A, C) and then moveDisks(n - 1, C, A). The key is realizing that we always have a tower to act as a buffer.
"""

# 8.7 Permutations without Dups
"""
Problems: Write a method to compute all permutations of a string of unique characters.

Solution: Pass an index as a parameter as well as the string. Take the str[index] pre-append and append to the
remaining string, then reverse the string and do the same. All while making sure that the string already does not exist
in a list that is being compiled. Then increment the index until == len(str). 
"""

# 8.9 Parens
"""
Problem: Implement an algorithm to print all valid (properly opened and closed) combintations
of n pairs of parentheses.

Example
Input: 3
Output: ((())), (()()), (())(), ()(()), ()()()

Solution: Using a list of len == input number have each index filled with (). Then working backwards 
starting from the last index place one () inside each previous () each time creating a new set and appending it to a new list.
Once the first run is done aka when we reach the first () or index = 0 then use the parentheses from index n and n - 1 to plug 
into every previous () => (()()) until you reach index = 0 then again append to new list. Repeat this until 
you plug in n - 1 * ()'s into the first (). Then stack n and n-1 onto each other and repeat the same process above. 

Simpler Solution: passing remaining left and right number of parentheses to the method signature you recurse by doing
if left < 0 or right < left then return, if left == 0 and right == 0 then copy the string, else
add left "(" then recurse with left - 1 and then add ")" then recurse right - 1.
"""

# 8.10 Paint Fill
"""
Problem: Implement the "paint fill" function that one might see on many image editing programs.
Given a screen (represented by 2D array of colors), a point, and a new color. Fill in surrounding 
area until the color changes from the original color. 

Solution: Create a recursive method thats base case is if at the given location the indicies are either
out of bounds, the point equals the new color or is not equal to the original color. Otherwise,
change the color of the current index then try recursing up, down, left, and right. 
"""

# 8.11 Coins
"""
Problem: Given an infinite number of quarters (25 cents), dimes (10 cents), nickles (5 cents), and
pennies (1 cent), write code to calculate the number of ways representing n cents.

Solution: Similar to the classic Backpack problem pass through as parameters counters
q: quaters, d: dimes, n:nickles, p:pennies, and a list to contain the different combintations.
Base case will be when n == 0 add the tuple of (q,d,n,p) to the list and return it, otherwise 
use a series of if-elif statements to do if n - 25 > 0 then then recurse with the
value of n decremented by 25 and the counter q incremented by 1. Then return the length of the list.

Optimization: Would be to use memoization to store the number of ways aka len(list) per amount if we end up calling
different total cent numbers.
"""

# 8.12 Eight Queens
"""
Problem: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
so that none of them share the same row, col, or diagonals.

Solution: Pass through the parameters a list of locations for 8 queens on the board starting at the bottom right corner.
Also pass through a list that contains lists which contain correct locations for all 8 queens, and another list that contains 
a list of positions that are not proper solutions. Implmenet method to check whether you can place a queen in a certain location.
Then have a base case where all queens are placed, where its the 8th queen and you cannot place it anywhere (still loop through all the other queens
if you cant place them even before the 8th). If you can place a queen, then recurse by decrementing the next queens location
by either one up, down, or diagonal (will also need a counter to know which queen to try and place next within param).
"""