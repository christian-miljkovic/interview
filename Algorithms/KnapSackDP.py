"""
KnapSack problem using dynamic programming
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack
"""

def knapsack(totalWeight, weightList, valueList, index, lookUpTable):

    if(totalWeight == 0 or index == 0):
        return 0

    # Do not include the value in this index
    elif(weightList[index-1] > totalWeight):
        return knapsack(totalWeight, weightList, valueList, index-1, lookUpTable)

    elif((totalWeight,index-1) in lookUpTable.keys()):
        return lookUpTable[totalWeight,index-1]    
    
    else:
        # Get the max of keeping the value at index - 1 or continue without it 
        answer = max(valueList[index-1] + knapsack(totalWeight - weightList[index - 1],weightList, valueList, index - 1, lookUpTable),
                                    knapsack(totalWeight, weightList, valueList, index - 1, lookUpTable)
        )
        lookUpTable[totalWeight,index-1] = answer
        return answer


if __name__ == '__main__':
    values = [60, 100, 120] 
    weights = [10, 20, 30] 
    totalWeight = 50
    n = len(values)
    lookUpTable = dict()
    print(knapsack(totalWeight, weights, values, n, lookUpTable))