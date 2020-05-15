# https://codeforces.com/contest/1352/problem/E



########## My O(n^2) solution which gives TLE (Pretty weird. Very strict time constraints) #########
# t = int(input())

# while t > 0:
#     t -= 1

#     n = int(input())
#     nums = list(map(int, input().split(" ")))

#     copy = nums.copy()

#     prev = 0
#     for i in range(len(nums)):
#         nums[i] = nums[i] + prev
#         prev = nums[i]
#     # print(nums)
#     ans = 0
#     for j in range(len(copy)):
#         d = {}
#         k = copy[j]
#         # print("K: ", k)
#         prev = 0
#         for i in range(len(nums)):
#             # print(d, nums[i])
            
#             if (nums[i] - k) in d.keys():
#                 # print("Got ans")
#                 ans += 1
#                 break
            
            
#             if prev in d.keys():
#                 d[prev] += 1
#             else:
#                 d[prev] = 1
            
#             prev = nums[i]
#         # print(d)
            
            
#     print(ans)



###### This O(n^2) solution that I saw from editorial works #########
from collections import defaultdict
t = int(input())

while t > 0:
    t -= 1

    n = int(input())
    nums = list(map(int, input().split(" ")))

    d = defaultdict(int)

    for i in range(len(nums)):
        d[nums[i]] += 1

    ans = 0
    for i in range(len(nums)):
        sum_ = nums[i]
        for j in range(i+1, len(nums)):
            sum_ += nums[j]

            if sum_ <= n:
                ans += d[sum_]
                d[sum_] = 0
    
    print(ans)