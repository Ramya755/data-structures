class Solution:
    def bubbleSort(self,arr):
        for i in range(len(arr)):
            isSwaped=False
            for j in range(0,len(arr)-i-1):
                if arr[j+1]<arr[j]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    isSwaped=True
            if not isSwaped:
                return arr
sol=Solution()
print(sol.bubbleSort([1,5,9,4,2,4,15,67,8,9]))
            
                    