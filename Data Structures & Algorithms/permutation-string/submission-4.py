class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = 0
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        if len(s1) > len(s2):
            return False
        while j < len(s1):
            freq1[s1[j]] += 1
            freq2[s2[j]] += 1
            j += 1
        if freq1 == freq2:
            return True
        while j < len(s2):
            freq2[s2[i]] -= 1
            if s2[j] in freq2:
                freq2[s2[j]] += 1
            else:
                freq2[s2[j]] = 1
            if freq2[s2[i]] == 0:
                del freq2[s2[i]]
            if freq1 == freq2:
                return True
            i += 1
            j += 1
        return False

            
            