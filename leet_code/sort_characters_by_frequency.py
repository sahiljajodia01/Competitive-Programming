# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3337/


###### My solution using normal sorting technique. Will be time O(n) and space O(1) since there are maximum 46 distinct chars.
class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        
        for i in range(len(s)):
            if s[i] in d.keys():
                d[s[i]] += 1
            else:
                d[s[i]] = 1
                
        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        
        ans = []
        for key, value in sorted_d:
            ans += [key] * value
            
        return ''.join(ans)


###### More efficient solution using bucket sort #######
class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        
        for i in range(len(s)):
            if s[i] in d.keys():
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        
        bucket = [[] for i in range(len(s)+1)]
        
        for i in d.keys():
            bucket[d[i]].append(i)
            
        
        ans = ""
        for i in range(len(bucket)-1, -1, -1):
            for j in bucket[i]:
                ans += j * i
        
        return ans