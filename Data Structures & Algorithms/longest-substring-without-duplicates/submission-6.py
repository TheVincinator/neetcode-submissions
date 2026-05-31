class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        maxLength = 0
        found = set()
        while i < len(s):
            while s[i] in found:
                found.remove(s[j])
                j += 1
            found.add(s[i])
            maxLength = max(maxLength, i - j + 1)
            i += 1
        return maxLength


