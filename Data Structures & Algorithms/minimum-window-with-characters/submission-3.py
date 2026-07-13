class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = defaultdict(int)
        need = 0
        for c in t:
            if c not in tMap:
                need += 1
            tMap[c] += 1

        have = 0
        sMap = defaultdict(int)
        res = ""
        j = 0
        for i in range(len(s)):
            if have == need:
                res = s[i:j] if len(res) == 0 or len(s[i:j]) < len(res) else res
            while j < len(s) and have != need:
                if s[j] in tMap:
                    sMap[s[j]] += 1
                    if sMap[s[j]] == tMap[s[j]]:
                        have += 1
                j += 1
                if have == need:
                    res = s[i:j] if len(res) == 0 or len(s[i:j]) < len(res) else res
            if s[i] in tMap:
                sMap[s[i]] -= 1
                if sMap[s[i]] < tMap[s[i]]:
                    have -= 1
        return res
