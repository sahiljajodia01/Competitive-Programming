# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/794/


###### It wierdly performs not so good. It is accepted though ######
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def solve(n, output, ans, a, b, num):
            if n == 0:
                output.append(ans)
            else:
                if a < num and b <= a:
                    solve(n-1, output, ans + "(", a+1, b, num)
                if b < num and a != 0:
                    solve(n-1, output, ans + ")", a, b+1, num)
                    
                    
        solve(2*n, output, "", 0, 0, n)
        
        return output