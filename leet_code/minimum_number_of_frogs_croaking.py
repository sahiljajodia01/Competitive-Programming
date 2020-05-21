# https://leetcode.com/contest/weekly-contest-185/problems/minimum-number-of-frogs-croaking/

####### I misunderstood the problem at first. I thought that we need to calculate the number of c-r-o-a-k subsequences in
####### the given string. But anyway I just slightly modify my code for the actual answer
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        chr_d = {"c":1, "r":2, "o":3, "a":4, "k":5}
        
        d = {1:0, 2:0, 3:0, 4:0, 5:0}
        count = 0
        curr = 0
        ans = 0
        for i in range(len(croakOfFrogs)):
            char = croakOfFrogs[i]
            
            if chr_d[char] == 1:
                d[chr_d[char]] += 1
                count += 1
                curr += 1
            else:
                if d[chr_d[char]-1] > 0:
                    d[chr_d[char]-1] -= 1
                    d[chr_d[char]] += 1
                    
                    if chr_d[char] == 5:
                        d[chr_d[char]] = 0
                        curr -= 1
                    
                    count += 1
                
            ans = max(ans, curr)
            
        for i in d.keys():
            count -= i * d[i]

        ############### To find the number of different c-r-o-a-k subsequences in the string, return count // 5 ###########
        
        if count == len(croakOfFrogs):
            return ans
        else:
            return -1