# https://leetcode.com/contest/weekly-contest-172/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        copy = num
        digit_arr = []
        while copy != 0:
            temp = copy % 10
            digit_arr.append(temp)
            copy = copy//10
            
        digit_arr = digit_arr[::-1]
        
        for i in range(len(digit_arr)):
            if digit_arr[i] == 6:
                digit_arr[i] = 9
                break
        digit_arr = digit_arr[::-1]
        # print(digit_arr)
        ini = 0
        multi = 1
        for i in range(len(digit_arr)):
            ini = ini + digit_arr[i]*multi
            # print(ini)
            multi *= 10
        
        return ini