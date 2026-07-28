class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freqs = defaultdict(int)
        for c in s:
            freqs[c] += 1
        
        lastIndices = defaultdict(int)
        for i, c in enumerate(s):
            freqs[c] -= 1
            if not freqs[c]:
                lastIndices[c] = i

        res = []
        i = 0
        lastIndex = 0
        for j, c in enumerate(s):
            lastIndex = max(lastIndex, lastIndices[c])
            if j == lastIndex:
                res.append(j - i + 1)
                i = j + 1
            j += 1
        
        return res



        