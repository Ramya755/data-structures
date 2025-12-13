class Solution(object):
    def canWinNim(self, n):
        return n%4!=0
sol=Solution()
print(sol.canWinNim(16))