"""
Input: sentence: string, queries: list
Edge Cases:
- empty input lists
- empty strings in queries
- duplicates in sentence
- invalid type 

Assumptions:
- are that words are all lowercase both in sentence and queries 
- string and queries contain valid type str
- there are not duplicate queries

Output: list of tuples indicates where word was found 

"""




# Q1: Given a sentence and set of query words, return the words present in the sentence and their word indices. The sentence will be all lowercase with no punctuation.

sentence = "Can i book a haircut haircut and blowout tomorrow with sarah"
#            0  1  2   3   4        5     6     7       8      9     10
            
queries = ['haircut', 'blowout', 'dog', 'sarah']

expected_result = [('haircut', 4), ('haircut', 5), ('blowout', 7), ('sarah', 10)]


        
def find_query(sentence, queries):
    
    if not sentence or not queries:
        return []
    
    query_set = list_to_set(queries)
    
    # To return values and index
    hash_map = dict()
    
    for index,word in enumerate(sentence.split()):
        if word in query_set:
            if word not in hash_map:
                hash_map[word] = [index]
            else:
                hash_map[word].append(index)
    
    return hash_map_to_list(hash_map)

def list_to_set(list_obj):
    
    # So that we can get O(1) lookups
    return_set = set()
    for word in list_obj:
        return_set.add(word)
        
    return return_set

def hash_map_to_list(hash_map):
    
    return_list = []
    for key, val in hash_map.items():
        for num in val:
            return_list.append((key,num))
            
    return return_list












# # Q2. Now there are misspellings. We provide a helper function similarity() that you are free to use. Feel free to copy/paste from the previouos section.

sentence_2 = "Can i book a haircut and blowoutt tomorrow with sarah and another blowout"
#            0  1  2   3   4      5     6        7      8     9
            
queries_2 = ['haircut', 'blowout', 'dog', 'sarah']

expected_result = [('haircut', 4), ('blowout', 6), ('sarah', 9)]




def similarity(word1, word2):
    # return a similarity score from 0 to 1
    # we consider the words similar if the score is > 0.8
    return float(len(set(word1).intersection(word2))) / len(set(word1).union(word2))



def list_to_sim_set(list_obj,split_list):
    
    return_set = set()
    
    for word in list_obj:
        return_set.add(word)
        for new_word in split_list:
            if is_similar(new_word, word):
                return_set.add(new_word)
        
    return return_set
    

def is_similar(word1, word2):
    
    return True if similarity(word1, word2) > 0.8 else False

def find_query_similarities(sentence, queries):
    
    if not sentence or not queries:
        return []
    
    split_list = sentence.split()
    similar_set = list_to_sim_set(queries,split_list)
    
    # To return values and index
    hash_map = dict()
    
    for index,word in enumerate(split_list):
        if word in similar_set:
            if word not in hash_map:
                hash_map[word] = [index]
            else:
                hash_map[word].append(index)
    
    return hash_map_to_list(hash_map)












# # Q3: Now query terms can N words long, for example "blow out". Feel free to copy/paste from the previous section.

# Assuming: query =  'blow out tomorrow'  != sentence = 'blowouttomorrow' or 
# query = 'blowout' != sentece = 'blow out' 

sentence_3 = "Can i book a haircut and blow outt tomorrow with sarah"
#            0  1  2   3   4      5   6     7     8      9    10
            
queries_3 = ['haircut', 'blow out tomroww', 'dog', 'sarah']

expected_result = [('haircut', 4), ('blow out', 6), ('sarah', 10)]


def list_to_len_map(query_list):
    
    hash_map = dict()
    
    for phrase in query_list:
        phrase_split = phrase.split()
        if len(phrase_split) not in hash_map:
            hash_map[len(phrase_split)] = [phrase_split]
        else:
            hash_map[len(phrase_split)].append(phrase_split)
    
    return hash_map
        
    
def check_with_window(size, phrase, sentence_list):
    
    count = 0
    return_list = []
    for i in range(len(sentence_list)):
    
        if sentence_list[i] == phrase[count] or is_similar(sentence_list[i], phrase[count]):
            count += 1
        else:
            count = 0
            
        if count == size:
            
            if size > 1:
                return_list.append((' '.join(phrase), i - size + 1))
            else:
                return_list.append((phrase[0], i - size + 1))
            count = 0
    
    return return_list
    
def find_query_len_n(sentence, queries):
    
    hash_map = list_to_len_map(queries)
    sentence_list = sentence.split()
    return_list = []
    for size, phrase_list in hash_map.items():
        for phrase in phrase_list:
            list_of_tuples = check_with_window(size, phrase, sentence_list)
            if list_of_tuples:
                return_list.extend(list_of_tuples)
    
    return return_list

if __name__ == '__main__':
    print(find_query(sentence, queries))
    print(find_query_similarities(sentence_2, queries_2))
    print(find_query_len_n(sentence_3, queries_3))