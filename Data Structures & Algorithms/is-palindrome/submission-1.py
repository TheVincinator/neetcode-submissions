class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        s = s.lower()
        new_s = []
        for c in s:
            if c in alphabet or c in numbers:
                new_s.append(c)
        new_s = "".join(new_s)
        def palindrome(s):
            if len(s) == 0 or len(s) == 1:
                return True
            if s[0] != s[-1]:
                return False
            return palindrome(s[1:len(s)-1])
        return palindrome(new_s)