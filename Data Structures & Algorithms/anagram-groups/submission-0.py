class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            freq = {}
            for l in s:
                if l not in freq:
                    freq[l] = 1
                else:
                    freq[l] += 1

            key = tuple(sorted(freq.items()))
            
            if key not in groups:
                groups[key] = [s]
            else:
                groups[key].append(s)
        return list(groups.values())