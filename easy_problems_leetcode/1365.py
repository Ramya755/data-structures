class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        p=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    c=c+1
            p.append(c)
        return p
sol=Solution()
print(sol.smallerNumbersThanCurrent([6,5,4,8]))