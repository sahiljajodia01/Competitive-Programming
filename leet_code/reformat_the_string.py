# https://leetcode.com/contest/weekly-contest-185/problems/reformat-the-string/

class Solution:
    def reformat(self, s: str) -> str:
        digit = []
        letter = []
        
        for i in range(len(s)):
            if s[i].isdigit():
                digit.append(s[i])
            else:
                letter.append(s[i])
        
        if len(digit) > len(letter)+1 or len(letter) > len(digit)+1:
            return ""
        
        final = []
        p1 = 0
        p2 = 0
        
        flag = True
        if len(digit) > len(letter):
            final.append(digit[p1])
            p1 += 1
            flag = False
        elif len(digit) < len(letter):
            final.append(letter[p2])
            p2 += 1
            flag = True
        
        while p1 < len(digit):
            if flag == False:
                final.append(letter[p2])
                final.append(digit[p1])
            else:
                final.append(digit[p1])
                final.append(letter[p2])
            p2 += 1
            p1 += 1
        
        return ''.join(final)