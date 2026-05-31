class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        maxLength = 0
        found = set()
        while i < len(s):
            if s[i] not in found:
                found.add(s[i])
            else:
                maxLength = max(maxLength, i - j)
                while s[i] in found:
                    found.remove(s[j])
                    j += 1
                found.add(s[i])
            i += 1
        maxLength = max(maxLength, i - j)
        return maxLength


