class Solution:
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[0]) - 1  
            while left <= right:
                mid = (left + right) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
ans=Solution()
print(ans.searchMatrix([[1,2,3],[2,3,4],[34,47,54]], 54))

