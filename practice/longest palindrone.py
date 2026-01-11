from collections import Counter
class Solution:
    def longestPalindrone(self,s):
        s=Counter(s)
        l=0
        odd=False
        for i in s.values():
            if i%2==0:
                l+=i
            else:
                l+=i-1
                odd=True
        if odd:
            return l+1
        else:
            return l
sol=Solution()
print(sol.longestPalindrone("abccccdd"))
