# Class for Prefix Tree or Trie

class Trie:

    def __init__(self, isSuffix=False):
        self.root = TrieNode(None)
        # Determines if we are creating a regular Trie or Suffix Trie
        self.isSuffix = isSuffix
    
    def insert(self, word):
        if(not self.isSuffix):
            self.insertInternal(word)
        else:
            listOfSuffixes = self.createAllSuffixes(word)
            listOfSuffixes.append(word)
            for suffix in listOfSuffixes:
                self.insertInternal(suffix)


    def createAllSuffixes(self, word):
        
        if(len(word) <= 1):
            return [word]

        listOfSuffixes = []
        for index in range(len(word) - 1, 0, -1):
            listOfSuffixes.append(word[index:])
        
        return listOfSuffixes
        
    def insertInternal(self, word):
        # dictionary of all the roots children 
        temp_trie = self.root
        for char in word:
            children = temp_trie.children
            if(char not in children):
                children[char] = TrieNode(char)
                temp_trie = children[char]
            else:
                temp_trie = children[char]
        
        temp_trie.isCompleteWord = True

    def find(self, word):
        
        temp_trie = self.root
        for char in word:
            if(char not in temp_trie.children):
                return False
            temp_trie = temp_trie.children[char]
        
        if(temp_trie.isCompleteWord):
            return True
        else:
            return False


    def toString(self):
        self.dfs(self.root)
    
    def printLetterAndChildren(self, root):
        childList = []
        for children in root.children:
            childList.append(children)
        print(root.letter, childList)
        print()

    def dfs(self, root):
        self.printLetterAndChildren(root)
        for child in root.children:
            childNode = root.children[child]
            self.dfs(childNode)
            


class TrieNode:

    def __init__(self,letter):
        self.letter = letter
        self.children = dict()
        self.isCompleteWord = False

testTrie = Trie()
testTrie.insert('hello')
testTrie.insert('hey')
testTrie.toString()
print(testTrie.find('he'))
print(testTrie.find('hello'))

testSuffixTrie = Trie(True)
testSuffixTrie.insert('hello')
testSuffixTrie.toString()
print(testSuffixTrie.find('ell'))