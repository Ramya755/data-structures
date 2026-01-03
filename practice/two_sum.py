class Solution:
    def two_sum(self,arr,target):
        hashmap={}
        for i,num in enumerate(arr):
            c=target-num
            if c in hashmap:
                return[hashmap[c],i]
            hashmap[num]=i
sol=Solution()
print(sol.two_sum([2,3,4,5,6,7,1],3))
