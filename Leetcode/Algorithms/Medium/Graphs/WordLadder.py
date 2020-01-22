"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""

# Time Compelxity: O(m*n) where m is len of each str
# Space Complexity: O(m*n) 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        word_list = collections.deque(wordList)
        graph = generate_graph(word_list)
        
        queue = collections.deque()
        queue.append((beginWord,1))
        is_visited = dict()
        is_visited[beginWord] = True
        
        while queue:
            
            word, level = queue.popleft()
            interim_words = get_interim_words(word)
            
            for interim_word in interim_words:
                
                if interim_word in graph:
                    for new_word in graph[interim_word]:
                        if new_word not in is_visited:
                            if new_word == endWord:
                                return level + 1

                            queue.append((new_word, level + 1))
                            is_visited[new_word] = True

                graph[interim_word] = []
        
        return 0
            
        
def generate_graph(word_list):
    
    graph = dict()
    
    for word in word_list:
        
        interim_words = get_interim_words(word)
        
        for interim in interim_words: 
            if interim not in graph:
                graph[interim] = [word]
            else:
                graph[interim].append(word)
    
    return graph    


def get_interim_words(word):
    
    words_list = []
    
    for i in range(len(word)):
            list_word = list(word)
            list_word[i] = '*'
            words_list.append(''.join(list_word))
    return words_list
            
            
            


# Initial Attempt trying to do problem with a Dijkstra approach

import heapq

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        word_list = collections.deque(wordList)
        word_list.appendleft(beginWord)
        graph = generate_graph(word_list)
        path = find_shortest_path(graph, beginWord, endWord)
        return 0 if path[endWord] == float('inf') else path[endWord] + 1
        
        
def find_shortest_path(graph, source, target):
    
    is_visited = dict()
    distance = dict()
    queue = collections.deque()
    heap = []
    heapq.heapify(heap)
    
    for node in graph:
        distance[node] = float('inf')    
    distance[source] = 0
    
    for node in graph:
        heapq.heappush(heap, (node, distance[node]))
        
    queue.append(source) 
    is_visited[source] = True
    
    while queue:
        
        node = queue.popleft()
        dist = distance[node]
        
        for child in graph[node]:
            
            if child not in is_visited:
                queue.append(child)
                if dist + 1 < distance[child]:
                    distance[child] = dist + 1
                is_visited[child] = True
    
    return distance
        
        
        
def generate_graph(word_list):
    
    graph = dict()
    sorted_words = sorted(word_list, key=lambda x: size_diff(word_list[0], x))
    print(sorted_words)
    for i, word in enumerate(word_list):
        graph[word] = set()
        for j, next_word in enumerate(word_list, i):
            if has_path(word, next_word):
                graph[word].add(next_word)
                
    return graph
    
    
def has_path(word_one, word_two):
    
    total_diff = 0
    for i in range(len(word_one)):
        if word_one[i] != word_two[i]:
            total_diff += 1
            
    return False if total_diff > 1 else True


def size_diff(word_one, word_two):
    total_diff = 0
    for i in range(len(word_one)):
        if word_one[i] != word_two[i]:
            total_diff += 1
            
    return total_diff