class Solution:
    def isPalindrome(self, s: str) -> bool:
        ordered = list(s.lower())
        for c in ordered.copy():
            if not c.isalnum():
                ordered.remove(c)
        rev = ordered.copy()
        rev.reverse()
        return ordered == rev
