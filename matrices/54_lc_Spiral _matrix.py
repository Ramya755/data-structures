class Solution(object):
    def spiralOrder(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        left=0
        right=m-1
        top=0
        bottom=n-1
        a=[]
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                a.append(matrix[top][i])
            top+=1
            for j in range(top,bottom+1):
                a.append(matrix[j][right])
            right-=1
            if top<=bottom:
                for k in range(right,left-1,-1):
                    a.append(matrix[bottom][k])
                bottom-=1
            if left<=right:
                for l in range(bottom,top-1,-1):
                    a.append(matrix[l][left])
                left+=1
        return a
sol=Solution()
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
        
        