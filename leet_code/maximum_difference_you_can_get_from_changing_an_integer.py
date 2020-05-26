class Solution:
    def maxDiff(self, num: int) -> int:
        digits = []
        
        copy = num
        while copy > 0:
            temp = copy % 10
            digits.append(temp)
            copy = copy // 10
            
        digits = digits[::-1]
        
        # print(digits)
        
        
        
        if digits[0] > 1:
            x = digits[0]
            y = 1
        else:
            x = 0
            y = 0
            for i in range(1, len(digits)):
                if digits[i] > 1:
                    x = digits[i]
                    break
        new_num = []
        for i in range(len(digits)):
            if digits[i] == x:
                new_num.append(y)
            else:
                new_num.append(digits[i])
        
        
        
        if digits[0] < 9:
            x = digits[0]
            y = 9
        else:
            x = 9
            y = 9
            for i in range(1, len(digits)):
                if digits[i] < 9:
                    x = digits[i]
                    break
                    
        new_num2 = []
        for i in range(len(digits)):
            if digits[i] == x:
                new_num2.append(y)
            else:
                new_num2.append(digits[i])
        
        # print(new_num, new_num2)
        
        digit1 = 0
        digit2 = 0
        for i in range(len(digits)-1, -1, -1):
            digit1 += new_num[i] * (10 ** (len(digits) - i -1))
            digit2 += new_num2[i] * (10 ** (len(digits) - i -1))
        
        
        
        return digit2 - digit1