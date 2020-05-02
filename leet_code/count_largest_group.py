# https://leetcode.com/problems/count-largest-group/

######## Easy problem
class Solution:
    def countLargestGroup(self, n: int) -> int:
        ans = []
        
        for i in range(1, n+1):
            sum_ = 0
            while i != 0:
                digit = i % 10
                sum_ += digit
                i = i//10
            
            if sum_ > len(ans):
                for i in range(len(ans), sum_):
                    ans.append([])
            
            ans[sum_-1].append(i)
            
        sorted_arr = sorted(ans, key=lambda x: len(x), reverse=True)
        
        count = 1
        
        max_ = len(sorted_arr[0])
        
        for i in range(1, len(sorted_arr)):
            if len(sorted_arr[i]) == max_:
                count += 1
        
        return count