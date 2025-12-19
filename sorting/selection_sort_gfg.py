class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            min_=i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[min_]:
                    min_=j
            arr[i],arr[min_]=arr[min_],arr[i]
        return arr
sol=Solution()
print(sol.selectionSort([4,1,2,5,7,8,9,10,2,3]))
#tc=o(n*2)