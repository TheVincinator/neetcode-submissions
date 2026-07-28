class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndices = {}
        for i, c in enumerate(s):
            lastIndices[c] = i

        res = []
        i = 0
        lastIndex = 0
        for j, c in enumerate(s):
            lastIndex = max(lastIndex, lastIndices[c])
            if j == lastIndex:
                res.append(j - i + 1)
                i = j + 1
        
        return res



        