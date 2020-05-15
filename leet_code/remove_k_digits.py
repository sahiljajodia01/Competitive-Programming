# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:        
        arr = []
        num = list(num)
        counter = 0
        
        while k > 0 and counter < len(num):
        # for i in range(len(num)):
            # print(counter)
            if len(arr) == 0:
                arr.append(num[counter])
            else:
                if num[counter] < arr[-1]:
                    while len(arr) > 0 and num[counter] < arr[-1] and k > 0:
                        if arr[-1] != '0':
                            k -= 1
                        arr.pop()
                    arr.append(num[counter])
                else:
                    arr.append(num[counter])
            counter += 1
        
        while k > 0 and len(arr) > 0:
            arr.pop()
            k -= 1
        
        counter1 = 0
        for i in range(len(arr)):
            if arr[i] == '0':
                counter1 += 1
            else:
                break
        
        
        # print(arr, num[counter:])
        final = ''.join(arr[counter1:] + num[counter:])
        if final == '':
            return '0'
        
        return ''.join(final)