# Recursive Algorithm to compute the length of the longest common subsequence

def longCommonSub(sequenceOne, sequenceTwo, n, m):
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
        return 1 + longCommonSub(sequenceOne, sequenceTwo, n-1, m-1)
    else:
        return max(longCommonSub(sequenceOne,sequenceTwo,n-1,m), longCommonSub(sequenceOne,sequenceTwo,n,m-1))


if __name__ == '__main__':
    testSequenceOne = "AGGTAB"
    testSequenceTwo = "GXTXAYB"
    print(longCommonSub(testSequenceOne,testSequenceTwo,len(testSequenceOne),len(testSequenceTwo)))