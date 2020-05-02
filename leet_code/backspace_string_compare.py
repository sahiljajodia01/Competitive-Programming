# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3291/

######### My solution using two stacks for 2 different strings
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack = []
        for i in range(len(S)):
            if S[i] == '#':
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(S[i])
        
        string1 = ''.join(stack)
        
        stack = []
        for i in range(len(T)):
            if T[i] == '#':
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(T[i])
        string2 = ''.join(stack)
        
        return string1 == string2

######## Another solution wherein you start from the reverse and skip the non hash character the number of times your encounter the hash character.
######## It will use only constant space.