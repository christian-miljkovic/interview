# Recursive Algorithm to compute the length of the longest common subsequence
import collections

def longCommonSub(sequenceOne, sequenceTwo, n, m, lookUpTable):
    """
    @sequenceOne: string sequence to compare
    @sequenceTwo: string sequence to compare
    @n: length of sequence one which also acts as an index
    @m: length of sequence two which also acts as an index
    """

    if(n == 0 or m == 0):
        return 0
    # we do n-1 and m-1 because on the first run we are inputing len(seqOne) which could be 3 if we have 'abc'
    # but to properly index we would want the index to be 2
    elif(sequenceOne[n-1] == sequenceTwo[m-1]):
        if([sequenceOne[n-1],sequenceTwo[m-1]] not in lookUpTable.keys()):
            lookUpTable[sequenceOne[n-1],sequenceTwo[m-1]] = n-1
        return 1 + longCommonSub(sequenceOne, sequenceTwo, n-1, m-1,lookUpTable)
    else:
        return max(longCommonSub(sequenceOne,sequenceTwo,n-1,m,lookUpTable), longCommonSub(sequenceOne,sequenceTwo,n,m-1,lookUpTable))


if __name__ == '__main__':
    testSequenceOne = "AGGTAB"
    testSequenceTwo = "GXTXAYB"
    lookUpTable = collections.OrderedDict()
    print(longCommonSub(testSequenceOne,testSequenceTwo,len(testSequenceOne),len(testSequenceTwo),lookUpTable))
    longestStr = ""
    for key, val in reversed(lookUpTable):
        longestStr += key[0]
    print(longestStr)   
