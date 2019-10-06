# https://leetcode.com/problems/plus-one/
# Google

def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1): 
        if digits[i] < 9:
            digits[i] += 1
            break
        else:
            digits[i] = 0
            if i == 0:
               digits.insert(0, 1) 

    print(digits)


plusOne([9, 9, 3, 9, 9])
