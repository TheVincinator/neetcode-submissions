class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        i = 0
        j = 0
        while j < len(s):
            if s[j] in charSet:
                res = max(res, j - i)
                while s[j] in charSet:
                    charSet.remove(s[i])
                    i += 1
            charSet.add(s[j])
            j += 1
        res = max(res, j - i)
        return res


