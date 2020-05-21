# https://leetcode.com/contest/weekly-contest-185/problems/display-table-of-food-orders-in-a-restaurant/


from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = {}
        food_item = {}
        t = {}
        for i in range(len(orders)):
            person, table, food = orders[i]
            
            if food not in food_item.keys():
                food_item[food] = 1
                
            if table not in d.keys():
                d[table] = defaultdict(int)
            
            if int(table) not in t.keys():
                t[int(table)] = 1
            
            d[table][food] += 1
        
        ans = [[0 for i in range(len(food_item)+1)] for j in range(len(d)+1)]
        
        food_item = {k:v for k,v in sorted(food_item.items())}
        
        t = sorted(t.items())
        print(food_item, t)
        ans[0][0] = "Table"
        count = 1
        
        for i in t:
            ans[count][0] = str(i[0])
            count += 1
        
        count = 1
        for food in food_item.keys():
            ans[0][count] = food
            for i in range(1, len(d)+1):
                ans[i][count] = str(d[ans[i][0]][food])
            count += 1
        
        return ans