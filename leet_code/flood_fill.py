# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/


###### BFS approach. It can also be done without using visited array ######
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # q = deque()
        q = []
        q.append([sr, sc])
        center_color = image[sr][sc]
        
        visited = []
        for i in range(len(image)):
            temp = []
            for j in range(len(image[0])):
                temp.append(0)
            
            visited.append(temp)
        
        while q:
            # print(q)
            # row, col = q.popleft()
            temp = []
            for i in range(len(q)):
                row, col = q[i]
                image[row][col] = newColor
                neighbours = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                visited[row][col] = 1
                for n in neighbours:
                    x, y = n

                    new_row, new_col = row - x, col - y

                    if new_row >= 0 and new_row < len(image) and new_col >= 0 and new_col < len(image[0]) and image[new_row][new_col] == center_color and visited[new_row][new_col] != 1:
                        temp.append([new_row, new_col])
            
            q = temp
        
        return image