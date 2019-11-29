# https://leetcode.com/discuss/interview-question/356960

def two_sum_modification(nums, target):
    # target = target - 30
    d = {}

    largest = 0
    ans = [-1, -1]
    for i in range(len(nums)):
        if ((nums[i] > largest) or ((target - nums[i]) > largest)) and ((target - nums[i]) in d.keys()):
            ans[0] = d[(target - nums[i])]
            ans[1] = i
            largest = max(nums[i], (target - nums[i]))
        d[nums[i]] = i

    return ans
