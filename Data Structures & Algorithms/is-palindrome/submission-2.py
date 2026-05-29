class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] not in chars:
                i += 1
            if s[j] not in chars:
                j -= 1
            if s[i] in chars and s[j] in chars:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
        return True