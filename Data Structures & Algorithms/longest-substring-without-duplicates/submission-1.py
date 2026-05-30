class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        maxLength = 0
        sub = ""
        while i < len(s):
            if s[i] not in sub:
                sub += s[i]
                i += 1
            else:
                maxLength = max(maxLength, len(sub))
                sub = sub[sub.find(s[i]) + 1:]
                sub += s[i]
                i += 1
        maxLength = max(maxLength, len(sub))
        return maxLength
        

