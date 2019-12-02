# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/


########### Sieve of Erathosthenes #############
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        
        arr = [-1] * n
        arr[0] = 0
        
        if n > 1:
            arr[1] = 1
        
        for num in range(2, len(arr)):
            if arr[num] == -1:
                for i in range((num+num), len(arr), num):
                    if i % num == 0:
                        arr[i] = i

        count = 0
        for i in range(len(arr)):
            if arr[i] == -1:
                count += 1
        
        return count