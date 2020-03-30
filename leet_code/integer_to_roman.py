# https://leetcode.com/problems/integer-to-roman/


######### A very naive approach. It beats only 8% of python submissions #########
from collections import deque

class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1: 'I', 2: 'II', 3: 'III', 5: 'V', 10: 'X', 20: 'XX', 30: 'XXX', 50: 'L', 100: 'C', 200: 'CC', 300: 'CCC', 500: 'D', 1000: 'M', 2000: 'MM', 3000: 'MMM'}
        original_number = [1, 5, 10, 50, 100, 500, 1000]
        
        
        copy = num
        q = deque()
        count = 1
        d_items = list(d.items())
        while copy != 0:
            temp = copy % 10
            temp *= count
            count *= 10
            copy = copy//10
            # print(temp)
            if temp == 0:
                continue
            for i in range(len(d_items)):
                if temp == d_items[i][0]:
                    q.appendleft(d[temp])
                    break
                elif temp < d_items[i][0]:
                    if (d_items[i][0]-temp) in original_number:
                        q.appendleft(d[d_items[i][0]])
                        q.appendleft(d[(d_items[i][0]-temp)])
                    else:
                        q.appendleft(d[(temp-d_items[i-1][0])])
                        q.appendleft(d[d_items[i-1][0]])
                    break

        # print('-----------------------')    
        return ''.join(q)




########## A simple but generalized and consice solution from the discussion forum #########
class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    
        d_items = list(d.items())
        arr = []
        for i in range(len(d_items)):
            while num >= d_items[i][0]:
                arr.append(d[d_items[i][0]])
                num -= d_items[i][0]
                
        return ''.join(arr)