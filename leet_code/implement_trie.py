# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3329/

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("")
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        # print(curr)
        for i in range(len(word)):
            if word[i] not in curr.children.keys():
                curr.children[word[i]] = TrieNode(word[i])
            curr = curr.children[word[i]]
        curr.word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children.keys():
                return False
            curr = curr.children[word[i]]
            
        if curr.word == True:
            return True
        
        return False
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] not in curr.children.keys():
                return False
            curr = curr.children[prefix[i]]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)