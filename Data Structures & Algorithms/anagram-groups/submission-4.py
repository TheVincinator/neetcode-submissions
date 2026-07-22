class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # { {a : 1, c : 1, t : 1} : ["act", "cat"]}
        dictionary = defaultdict(list)
        for s in strs:
            inner_dict = defaultdict(int)
            for c in s:
                inner_dict[c] += 1
            dictionary[tuple(sorted(inner_dict.items()))].append(s)
        print(dictionary)
        res = []
        for key in dictionary:
            res.append(dictionary[key])
        return res

