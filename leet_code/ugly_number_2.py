# https://leetcode.com/problems/ugly-number-ii/


######## BFS solution with DP (i.e  not add neighbours already added). Barely Works fine. Complexity is O(n)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        q = [2, 3, 5]
        count = 0
        while count < n:
            # print(q[count])
            temp = []
            ele = q[count]
            
            mul = [2, 3, 5]
            
            for i in mul:
                if ele * i not in q:
                    q.append((ele * i))
            
            q = sorted(q)
            
            count += 1
        return q[count-2]


######### An even better solution without using sorting. I found this solution in discussions ########
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        index2, index3, index5 = 0, 0, 0
        factor2, factor3, factor5 = 2, 3, 5
        
        dp = [-1]*(n+1)
        
        dp[0] = 1
        
        for i in range(1, n):
            # print(dp)
            minimum = min(factor2, factor3, factor5)
            dp[i] = minimum
            
            if factor2 == minimum:
                index2 += 1
                factor2 = 2 * dp[index2]
            if factor3 == minimum:
                index3 += 1
                factor3 = 3 * dp[index3]
            if factor5 == minimum:
                index5 += 1
                factor5 = 5 * dp[index5]
        
        return dp[n-1]



######## A slower solution using hashmaps. It gives TLE. Complexity is O(nth ugly number) which is very large ######
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        d = { 2: 1, 3: 1, 5: 1}
        prime = {}
        nth = 2
        count = 2
        curr = 3
        while count != n:
            # print(nth, curr, count, d)
            # print(prime)
            
            flag = False
            
            for key in prime.keys():
                if curr % key == 0:
                    flag = True
                    break
                    
            if flag == True:
                prime[curr] = 1
                curr += 1
                continue
            
            for key in d.keys():
                if curr % key == 0:
                    d[curr] = 1
                    count += 1
                    nth = curr
                    flag = True
                    break
            
            if flag == False:
                prime[curr] = 1
            
            curr += 1
        
        return nth