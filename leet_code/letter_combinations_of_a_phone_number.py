# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/793/


###### Backtracking solution #######
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2": ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i']
                , '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's']
                , '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        
        output = []
        def solve(digits, d, output, ans, minimum):
            if len(ans) == len(digits) and len(digits) != 0:
                output.append("".join(ans))
            else:
                for i in range(minimum, len(digits)):
                    for j in range(len(d[digits[i]])):
                        ans.append(d[digits[i]][j])
                        solve(digits, d, output, ans, i+1)
                        ans.pop()
        
        solve(digits, d, output, [], 0)
        return output