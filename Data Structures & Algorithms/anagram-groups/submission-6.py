class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # { [1,0,1,...] : ["act", "cat"]}
        dictionary = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            dictionary[tuple(count)].append(s)
        return list(dictionary.values())
