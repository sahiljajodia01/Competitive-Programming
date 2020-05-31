# https://leetcode.com/problems/satisfiability-of-equality-equations/


###### Union Find solution for this problem #######
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = []
        
        for i in range(26):
            parents.append(i)
        
        
        def find(x):
            root = x
            
            while root != parents[root]:
                root = parents[root]
            
            while parents[x] != root:
                n = parents[x]
                parents[x] = root
                x = n
            
            return root
        
        def union(x, y):
            par1 = find(x)
            par2 = find(y)
            
            if par1 == par2:
                return
            
            parents[par1] = par2
        
        ans = []
        
        for i in range(len(equations)):
            a, sign, b = equations[i][0], equations[i][1:3], equations[i][3]
            
            if sign == "==":
                union((ord(a) - ord('a')), (ord(b) - ord('a')))                             
                
        for i in range(len(equations)):
            a, sign, b = equations[i][0], equations[i][1:3], equations[i][3]
            
            if sign == "!=":
                if find((ord(a) - ord('a'))) == find((ord(b) - ord('a'))):
                    return False
        
        return True