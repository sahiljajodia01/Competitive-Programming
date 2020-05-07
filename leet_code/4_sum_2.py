# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/829/


###### This is the best solution for this problem. Only one new hashmap. As the range of values in arrays is from
###### -2^28 to 2^28+1.
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans = 0
        a_and_b = {}
        for i in range(len(A)):
            for j in range(len(B)):
                if (A[i] + B[j]) in a_and_b.keys():
                    a_and_b[(A[i] + B[j])] += 1
                else:
                    a_and_b[(A[i] + B[j])] = 1
    
        for i in range(len(C)):
            for j in range(len(D)):
                sum_ = C[i] + D[j]
                
                if (0 - sum_) in a_and_b.keys():
                    ans += a_and_b[(0 - sum_)]

        return ans
    

##### This solution uses two hashmaps for 4 arrays. It can be useful when the range of values in arrays is not that big.
##### Ans when the numbers of values in the arrays is very large
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans = 0
        a_and_b = {}
        c_and_d = {}
        for i in range(len(A)):
            for j in range(len(B)):
                if (A[i] + B[j]) in a_and_b.keys():
                    a_and_b[(A[i] + B[j])] += 1
                else:
                    a_and_b[(A[i] + B[j])] = 1
                    
                if (C[i] + D[j]) in c_and_d.keys():
                    c_and_d[(C[i] + D[j])] += 1
                else:
                    c_and_d[(C[i] + D[j])] = 1
        
        for i in a_and_b.keys():
            if (0 - i) in c_and_d.keys():
                ans += (a_and_b[i] * c_and_d[(0 - i)])
        
        return ans