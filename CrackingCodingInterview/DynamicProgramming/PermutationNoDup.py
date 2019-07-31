# 8.7 Permutations without Dups
# Problem: Write a method to compute all permutations of a string of unique characters.

def permutate(string, index):
    allPermutations = []
    if index != len(string):
        
        allPermutations = permutate(string, index + 1)

        newPermutations = []
        preAppendedStr, preAppendedRevStr = preAppendInternal(string.replace(string[index],""),string[index])
        appendedStr, appendedRevStr = appendInternal(string.replace(string[index],""),string[index])
        newPermutations.append(preAppendedStr)
        newPermutations.append(preAppendedRevStr)
        newPermutations.append(appendedStr)
        newPermutations.append(appendedRevStr)

        if allPermutations != None:
            for value in newPermutations: 
                if value not in allPermutations:
                    allPermutations.append(value)
        else:
            return newPermutations

        return allPermutations

def preAppendInternal(string, char):
    reversedStr = string[::-1]
    a = char + string
    b = char + reversedStr
    return a,b

def appendInternal(string, char):
    reversedStr = string[::-1]
    a = string + char
    b = reversedStr + char
    return (a,b)


if __name__ == "__main__":
    testStr = 'abcd'
    print(permutate(testStr,0))