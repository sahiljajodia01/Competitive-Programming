# https://leetcode.com/problems/range-sum-query-immutable/

# Init in O(n) and sumRange in O(1). Better solution because sumRange is called many times for same input.
class NumArray:

    def __init__(self, nums: List[int]):
        prev = 0
        sums = []
        for i in range(len(nums)):
            sums.append((prev + nums[i]))
            prev = sums[i]
        
        self.sums = sums

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sums[j]
        else:
            return (self.sums[j] - self.sums[i-1])


# Init in O(1) and sumRange in O(n).
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        total = 0
        for index in range(i, j+1):
            total += self.nums[index]
        
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)