# https://leetcode.com/contest/weekly-contest-172/problems/print-words-vertically/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        count = 0
        final_ans = []
        max_len = 0
        for i in range(len(words)):
            if len(words[i]) > max_len:
                max_len = len(words[i])
                
        for i in range(max_len):
            ans = ""
            for j in range(len(words)):
                if i >= len(words[j]):
                    ans += " "
                else:
                    ans += words[j][i]
            ans = ans.rstrip()
            final_ans.append(ans)
            
        return final_ans