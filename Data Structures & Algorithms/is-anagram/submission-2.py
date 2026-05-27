class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = defaultdict(int)
        tMap = defaultdict(int)
        for c in s:
            sMap[c] += 1
        for c in t:
            tMap[c] += 1
        return sMap == tMap