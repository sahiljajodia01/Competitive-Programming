# https://leetcode.com/problems/01-matrix/


######### Solves using BFS #########
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        q = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    q = [[i, j]]
                    count = 1
                    while q:
                        neighbors = [[-1, 0], [0, -1], [1, 0], [0, 1]]
                        temp = []
                        flag = False
                        for k in range(len(q)):
                            x, y = q[k]
                            for n in neighbors:
                                x1, y1 = x + n[0], y + n[1]

                                if x1 >= 0 and x1 < len(matrix) and y1 >= 0 and y1 < len(matrix[0]):
                                    if matrix[x1][y1] == 0:
                                        matrix[i][j] = count
                                        flag = True
                                        break
                                    else:
                                        temp.append([x1, y1])
                            if flag == True:
                                break
                        if flag == True:
                            break

                        q = temp
                        count += 1
        
        return matrix