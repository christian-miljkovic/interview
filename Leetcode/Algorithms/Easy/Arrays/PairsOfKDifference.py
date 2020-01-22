# Given a large array of ints return a list of pairs that have a difference 
# of constant k

def getPairs(arr, k):

    pairs_list = []

    hash_map = dict()

    for num in arr:
        if num not in hash_map:
            hash_map[num] = True

    for num in arr:
        if num + k in hash_map:
            pairs_list.append((num, num+k)) 
        if num - k in hash_map:
            pairs_list.append((num, num-k))
    
    return pairs_list

if __name__ == '__main__':
    test_array = [1,3,4,11,9,8,-2,-5]
    k = 3
    print(getPairs(test_array,k))