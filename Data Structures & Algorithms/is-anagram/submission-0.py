class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = list(s)
        w2 = list(t)
        w1.sort()
        w2.sort()
        if w1 == w2:
            return True
        return False