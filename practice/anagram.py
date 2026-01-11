from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        s=Counter(s)
        t=Counter(t)
        if t==s:
            return True
        return False
sol=Solution()
print(sol.isAnagram("anagram","jshduewiy"))
        