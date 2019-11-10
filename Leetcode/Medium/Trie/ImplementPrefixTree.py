"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.end_of_word = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self
        for char in word:
            if char not in temp.children:
                temp.children[char] = Trie()
            temp = temp.children[char]
        
        temp.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self
        for char in word:
            if char not in temp.children:
                return False
            temp = temp.children[char]
        
        return temp.end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self
        for char in prefix:
            if char not in temp.children:
                return False
            temp = temp.children[char]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)