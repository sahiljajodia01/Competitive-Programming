# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/

############ Elegant Hasmap solution #############
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        d = {3: 'Fizz', 5: 'Buzz'}
        for i in range(1, n+1):
            ans = ""
            for key, val in d.items():
                if i % key == 0:
                    ans += val
            
            if ans == "":
                arr.append(str(i))
            else:
                arr.append(ans)
        
        return arr

########## Niave If Else Solution ############
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        d = {3: 'Fizz', 5: 'Buzz'}
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                arr.append("FizzBuzz")
            elif i % 3 == 0:
                arr.append("Fizz")
            elif i % 5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(i))
                
        return arr