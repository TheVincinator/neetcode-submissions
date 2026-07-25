class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = defaultdict(int)
        res = 0
        i = 0
        j = 0
        while j < len(s):
            res = max(res, j - i)
            charDict[s[j]] += 1
            while j - i + 1 - max(charDict.values()) > k:
                charDict[s[i]] -= 1
                if charDict[s[i]] == 0:
                    del charDict[s[i]]
                i += 1
            j += 1
        res = max(res, j - i)
        return res