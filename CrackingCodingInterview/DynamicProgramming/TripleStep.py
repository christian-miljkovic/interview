"""
Chapter 8 - Recursion and Dynamic Programming
Problem - Triple Step: A child is running up a staircase with n steps and can hop either 
1, 2, or 3 steps at a time. Implement a method to count how many possible ways the child can run up
the stairs.
Time Complexity: O(3^n) without memoization
"""
def tripleStep(n, lookUpTable):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n in lookUpTable.keys():
        return lookUpTable[n]
    else:
        lookUpTable[n] = tripleStep(n-1, lookUpTable) + tripleStep(n-2, lookUpTable) + tripleStep(n-3, lookUpTable)
    
    return lookUpTable[n]

if __name__ == "__main__":
    steps = int(input())
    lookUpTable = dict()
    print(tripleStep(steps, lookUpTable))