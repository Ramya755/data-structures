class Solution(object):
    def setZeroes(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        col0=1
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    if j!=0:
                        matrix[0][j]=0
                    else:
                        col0=0
        for a in range(1,n):
            for b in range(1,m):
                if matrix[a][0]==0 or matrix[0][b]==0:
                    matrix[a][b]=0
        if matrix[0][0]==0:
            for r  in range(m):
                matrix[0][r]=0
        if col0==0:
            for l in range(n):
                matrix[l][0]=0
        return matrix
sol=Solution()
print(sol.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

