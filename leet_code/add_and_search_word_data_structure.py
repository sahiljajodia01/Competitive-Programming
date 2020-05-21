["WordDictionary","addWord","addWord","addWord","addWord","search","search","search","search","search","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["drd"],["pad"],["bad"],[".ad"],["b.."],["bm.."],["..m"],["d"],["b..."],["d.d"]]
["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
[[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]



class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word = False
    
    
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("")
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        # print(curr)
        for i in range(len(word)):
            if word[i] not in curr.children.keys():
                curr.children[word[i]] = TrieNode(word[i])
            curr = curr.children[word[i]]
        curr.word = True

    
    def dfs(self, word, i, curr):
        if i > len(word)-1:
            if curr.word == True:
                return True
            else:
                return False
        
        if word[i] != ".":
            if word[i] in curr.children.keys():
                return self.dfs(word, i+1, curr.children[word[i]])
            else:
                return False
        else:
            for j in curr.children.keys():
                return self.dfs(word, i+1, curr.children[j])
            else:
                return False
        
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        curr = self.root
        return self.dfs(word, 0, curr)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)