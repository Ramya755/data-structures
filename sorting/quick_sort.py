class Solution:
    def quickSort(self, arr, low, high):
        if low<high:
            p=self.partition(arr,low,high)
            self.quickSort(arr,low,p-1)
            self.quickSort(arr,p+1,high)
    def partition(self, arr, low, high):
        pivot=arr[low]
        i=low
        j=high
        while i<j:
            while arr[i]<=pivot and i<=high-1:
                i+=1
            while arr[j]>pivot and j>=low+1:
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        return j
sol=Solution()
arr=[1,5,9,4,2,4,15,67,8,9]
sol.quickSort(arr,0,len(arr)-1)
print(arr)         