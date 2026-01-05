from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        c=Counter(ransomNote)
        m=Counter(magazine)
        return not (c-m)
sol=Solution()
print(sol.canConstruct("a","b"))

