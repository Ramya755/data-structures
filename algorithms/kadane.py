class Solution:
    def maxSubarraySum(self, arr):
        max_=arr[0]
        cur_s=0
        for i in range(len(arr)):
            cur_s+=arr[i]
            max_=max(cur_s,max_)
            if cur_s<0:
                cur_s=0
        return max_
sol=Solution()
print(sol.maxSubarraySum([2,3,7,5,8,9,3]))