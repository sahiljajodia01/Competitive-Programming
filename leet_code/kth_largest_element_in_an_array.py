# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/800/

###### Again a hashmap follwed with sorting that hashmap. Complexity: O(n) + O(klogk) where k is number of distinct elements #####
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d.keys():
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        
        d_sorted = sorted(d.items(), key=lambda v: v[0], reverse=True)
        
        total = 0
        for key, value in d_sorted:
            total += value
            if k <= total:
                return key