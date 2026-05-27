class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            count = [0] * 26
            for l in s:
                count[ord(l) - ord('a')] += 1
            key = tuple(count)
            if key not in group:
                group[key] = [s]
            else:
                group[key].append(s)
        return list(group.values())