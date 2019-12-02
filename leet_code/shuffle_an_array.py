# https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/

######### A design question ##########
######### It is an interesting one. There can be other correct answers also #########
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        index_arr = [i for i in range(len(self.nums))]
        
        new_arr = []
        while index_arr != []:
            random_index = random.randint(0, len(index_arr)-1)
            random_num = self.nums[index_arr[random_index]]
            index_arr.pop(random_index)
            new_arr.append(random_num)
            
        return new_arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()