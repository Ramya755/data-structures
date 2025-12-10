class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for r in matrix:
            r.reverse()
        return matrix
sol=Solution()
print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))

        