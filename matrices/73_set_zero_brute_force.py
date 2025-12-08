class Solution(object):
    def setZeroes(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    for k in range(len(matrix[i])):
                        if matrix[i][k]!=0:
                            matrix[i][k]=-1
                    for l in range(len(matrix)):
                        if matrix[l][j]!=0:
                            matrix[l][j]=-1
        for a in range(len(matrix)):
            for b in range(len(matrix[0])):
                if matrix[a][b]==-1:
                    matrix[a][b]=0
        return matrix
sol=Solution()
print(sol.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,9]]))