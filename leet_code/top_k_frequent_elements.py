# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/

##### Creating a hashmap first. Then sorting it with respect to value. Time complexity: O(n) [hashmap] + O(klogk) [sorting] #####
##### Where k is number of distinct elements in hashmap ######
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d.keys():
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
                
        d_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)

        final_ans = []
        for i in range(k):
            final_ans.append(d_sorted[i][0])
            
        return final_ans