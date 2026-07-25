class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        s1Map = defaultdict(int)
        for i in range(len(s1)):
            s1Map[s1[i]] += 1
        
        i = 0
        j = 0
        s2Map = defaultdict(int)
        while j < len(s2):
            while j < len(s1):
                s2Map[s2[j]] += 1
                j += 1
            if len(s1) == len(s2):
                return s1Map == s2Map
            if s1Map == s2Map:
                return True
            s2Map[s2[i]] -= 1
            if not s2Map[s2[i]]:
                del s2Map[s2[i]]
            i += 1
            s2Map[s2[j]] += 1
            j += 1
        return s1Map == s2Map
            