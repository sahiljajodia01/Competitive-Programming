# https://leetcode.com/contest/biweekly-contest-24/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/
###### For this problem I had to look the idea that we have to take a fibonacci number only once in the discussion. ######
###### After this it was easy ######


####### An okayish solution that only works till 99999. Complexity O(n) #######
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        nums = [1, 1]
        d = {1: 1}
        while nums[-1] < k:
            nums.append(nums[-1] + nums[-2])
            d[nums[-1]] = 1
        
        print(d)
        print(nums)
        count = k
        ans = 0
        while k > 0:
            # print(k, count)
            if count in d.keys():
                k -= count
                count = k
                ans += 1
            else:
                count -= 1
        
        return ans


####### Best solution with complexity of roughly O(logn) #######
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        ans = 0
        while k > 0:
            # print(k, ans)
            nums = [1, 1]
            while nums[-1] <= k:
                nums.append(nums[-1] + nums[-2])
            
            k -= nums[len(nums)-2]
            ans += 1
        
        return ans