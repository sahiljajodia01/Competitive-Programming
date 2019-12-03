# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

########### This the earlier approach that I used to solve the 3sum problem ############
# import pysnooper
# inp = input("Enter the numbers: ").split(" ")
# inp = [int(i) for i in inp]
# dic = {}

# for i in inp:
#     if i in dic.keys():
#         dic[i] += 1
#     else:
#         dic[i] = 1

# # @pysnooper.snoop()
# def main():
#     sol = []
#     for i in range(len(inp)):
#         for j in range(i+1, len(inp)):
#             temp1 = inp[i]
#             temp2 = inp[j]
#             f = -1 * (temp1 + temp2)
#             if f in dic.keys():
#                 if temp1 == f and temp2 == f:
#                     if dic[f] < 3:
#                         continue
#                 elif (temp1 == f and temp2 != f) or (temp2 == f and temp1 != f):
#                     if dic[f] < 2:
#                         continue
#                 arr = [temp1, temp2, f]
#                 arr.sort()             
#                 sol.append(arr)
#     print(sol)
#     print(list(map(list, list(set(map(tuple, sol))))))

# main()




########## Fixing one number and solving two sum problem using hash map on rest of array ###########
########## We can also solve the two sum problem using two pointer approach after sorting the array ##########
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol_set = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            d = {}
            for j in range(i+1, len(nums)):
                sol = [-1, -1, -1]
                if target - nums[j] in d.keys():
                    sol[0], sol[1], sol[2] = nums[i], (target - nums[j]), nums[j]
                    sol = sorted(sol)
                    sol_set.append(sol)
                d[nums[j]] = j
        
        return list(set(map(tuple, sol_set)))