# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/


######## solution without dictioanry ##########
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(len(s)):
            # print(stack)
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    top = stack.pop()
                    if (s[i] == ')' and top == '(') or (s[i] == ']' and top == '[') or (s[i] == '}' and top == '{') :
                        continue
                    else:
                        return False
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False


####### A little more elegant solution with dictionary #########
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(': ')', '[': ']', '{': '}'}
        
        for i in range(len(s)):
            if s[i] in d.keys():
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    top = stack.pop()
                    if s[i] != d[top]:
                        return False
                else:
                    return False
        
        return len(stack) == 0