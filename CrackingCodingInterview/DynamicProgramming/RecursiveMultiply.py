# Chapter 8
# Recursive Multiply
# Time Complexity: O(b)

def multiply(a, b):

    if a == 0 or b == 0:
        return 0
    elif b == 1:
        return a
    else:
        b -= 1
        a += multiply(a, b)
        return a

if __name__ == "__main__":
    print(multiply(4,2))
        