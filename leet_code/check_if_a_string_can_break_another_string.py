# https://leetcode.com/contest/biweekly-contest-25/problems/check-if-a-string-can-break-another-string/


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        arr = [0 for i in range(26)]
        for i in range(len(s2)):
            arr[(ord(s2[i]) - ord('a'))] += 1
        
        first = True
        for i in range(len(s1)):
            flag = False
            for j in range((ord(s1[i]) - ord('a')), len(arr)):
                if arr[j] > 0:
                    flag = True
                    arr[j] -= 1
                    break
            
            if flag == False:
                first = False
                break
        
        arr = [0 for i in range(26)]
        for i in range(len(s1)):
            arr[(ord(s1[i]) - ord('a'))] += 1
        
        
        second = True
        for i in range(len(s2)):
            flag = False
            for j in range((ord(s2[i]) - ord('a')), len(arr)):
                if arr[j] > 0:
                    flag = True
                    arr[j] -= 1
                    break
            
            if flag == False:
                second = False
                break
                
        if first or second:
            return True
        else:
            return False