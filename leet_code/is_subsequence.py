# https://leetcode.com/problems/is-subsequence/


######## There also could be a two pointer approach. String "s" and string "t" both have a pointer. You check
####### Whether string s have all characters in string t in increasing index else return false. This is a very naive
####### approach and the follow up question wouldn't accept this as an answer.



# A normal approach using the hashmap and finding if the index of next char is greater than the index of prev char
from collections import deque, defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        def binary_search(nums, start, end, target):
            if start <= end:
                mid = int(start + (end-start)/2)

                if nums[mid] < target:
                    binary_search(nums, mid+1, end, target)
                else:
                    binary_search(nums, start, mid-1, target)

            return nums[mid]


        t_dict = defaultdict(deque)
        
        for i in range(len(t)):
            t_dict[t[i]].append(i)
        # print(t_dict)
        prev = -1
        for i in range(len(s)):
            if s[i] in t_dict.keys():
                val = t_dict[s[i]]
                old_prev = prev
                for j in val:
                    if j > prev:
                        prev = j
                        break
                        
                if old_prev == prev:
                    return False
            else:
                return False
        
        return True



# Similar approach as above but using binary search to find the greater index from the hash map as values in hashmap
# are in sorted order. Surprisingly this approach does not work as well as I thought it should have worked. Only giving
# a 4 fold saving in time complexity which is less as compared to going from O(n*len_of_string) to O(logn*len_of_string).
from collections import deque, defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        def binary_search(nums, start, end, target, value):
            if start <= end:
                mid = int(start + (end-start)/2)

                if nums[mid] <= target:
                    return binary_search(nums, mid+1, end, target, value)
                else:
                    return binary_search(nums, start, mid-1, target, nums[mid])

            return value
        
        
        
        t_dict = defaultdict(deque)
        
        for i in range(len(t)):
            t_dict[t[i]].append(i)
        # print(t_dict)
        prev = -1
        for i in range(len(s)):
            # print("char: ", s[i])
            if s[i] in t_dict.keys():
                val = t_dict[s[i]]
                old_prev = prev
                prev = binary_search(val, 0, len(val)-1, old_prev, prev)

                if old_prev == prev:
                    return False
            else:
                return False
        
        return True