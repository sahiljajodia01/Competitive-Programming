# https://leetcode.com/problems/perfect-squares/

######## A BFS solution in which you take the element at front of queue and get all possible value by substracting squares
######## till it is greater than zero and put them in the queue. Continue this process till it you get zero as a value.
######## Return the count at that point. I had to read the discussions for this solution
class Solution:
    def numSquares(self, n: int) -> int:
        q = [n]
        count = 1
        while q != []:
            temp = []
            flag = False
            for i in range(len(q)):
                num = q.pop(0)
                curr = 1
                while (curr * curr) <= num:
                    x = num - (curr*curr)
                    if x == 0:
                        flag = True
                        break
                    temp.append(x)
                    curr += 1
                if flag == True:
                    break
            
            if flag == True:
                break
            q = temp
            count += 1
        
        return count

######### A couple of bottom up dp solutions. It gives TLE
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        
        dp[0] = 0
        
        for i in range(1, n+1):
            for j in range(1, i+1):
                if j*j <= i:
                    dp[i] = min(1 + dp[i-(j*j)], dp[i])
        
        return dp[-1]

        # total = 1
        # count = 0
        # sum_ = 0
        # while sum_ != n:
        #     total = 1
        #     while (total*total) <= n:
        #         total += 1
            
        #     count += 1
        #     sum_ += total
            
        
        # return count


######### A top down DP solution. It also gives TLE
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [9999999999] * (n+1)
        # max_ = [99999999]
        def solve(a, b, count):
            print(a, b, count, dp)
            if dp[b] != 9999999999:
                # print("Inside if")
                return dp[b]
            elif b == 0:
                return 0
            elif b < 0 or (a*a > b):
                return 9999999999
            else:
                # ans1, ans2 = 0, 0
                ans1 = 1 + solve(a, b-(a*a), count+1)
                ans2 = solve(a+1, b, count)
                dp[b] = min(ans1, ans2)
                # print("ans1: ", ans1, ", ans2: ", ans2)
                return dp[b]
                # return ans
        
        ans = solve(1, n, 0)
        return ans