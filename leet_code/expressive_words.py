# https://leetcode.com/problems/expressive-words/


########### Using a Trie based approach to solve this. This was asked in Pujan's interview with Google ###########
###### Other people have a totally different solution - https://leetcode.com/problems/expressive-words/discuss/?currentPage=1&orderBy=most_votes&query=
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
        self.count = 0
        
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
    
    def dfs(self, S, index, curr, extension, count):
        # print(index, count)
        if index > len(S)-1:
            if curr.word == True:
                self.count += 1
        else:
            
            if count < len(extension) and index >= extension[count][0] and index <= extension[count][1]:
                total = extension[count][1] - extension[count][0] + 1
                # print("Total: ", total)
                if total == 2:
                    if S[index] in curr.children.keys():
                        if S[index] in curr.children[S[index]].children.keys():
                            self.dfs(S, index + 2, curr.children[S[index]].children[S[index]], extension, count+1)
                else:
                    
                    for i in range(total):
                        if S[index] in curr.children.keys():
                            self.dfs(S, extension[count][1] + 1, curr.children[S[index]], extension, count+1)
                            curr = curr.children[S[index]]
            else:
                if S[index] in curr.children.keys():
                    self.dfs(S, index+1, curr.children[S[index]], extension, count)

        
    def search_extension(self, S, extension) -> int:
        curr = self.root
        
        self.dfs(S, 0, curr, extension, 0)
        
        return self.count
        


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        t = Trie()
        
        for i in range(len(words)):
            t.insert(words[i])
            
        extensions = []
        
        prev = ""
        p = 0
        for i in range(len(S)):
            if S[i] != prev:
                if (i-1) - p > 0:
                    extensions.append([p, i-1])
                
                p = i
            
            prev = S[i]
        
        if (len(S)-1) - p > 0:
            extensions.append([p, len(S)-1])
        # print(extensions)
        
        return t.search_extension(S, extensions)