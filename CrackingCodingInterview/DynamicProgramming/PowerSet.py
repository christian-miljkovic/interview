# 8.4
# Problem: Write a method to return all subsets of a set

def powerSet(sets, index):
    allSubsets = []
    if len(sets) == index:
        #base case - add empty set
        if [] not in allSubsets:
            allSubsets.append([])
    else:
        allSubsets = powerSet(sets, index+1)
        item = sets[index]
        moreSubsets = []
        for subset in allSubsets:
            newSubset = []
            [newSubset.append(value) for value in subset if value not in newSubset]
            newSubset.append(item)
            moreSubsets.append(newSubset)
        [allSubsets.append(value) for value in moreSubsets if value not in newSubset]
    return allSubsets


if __name__ == "__main__":
    test_set = [1,2,3,4]
    print(powerSet(test_set,0))