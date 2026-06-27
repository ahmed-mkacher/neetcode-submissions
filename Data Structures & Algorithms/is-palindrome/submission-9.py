class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = True
        i = 0
        j = len(s) - 1
        
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1 
                continue
            if s[i].lower() != s[j].lower():
                valid = False

                break

            i += 1
            j -= 1     
        
        return valid