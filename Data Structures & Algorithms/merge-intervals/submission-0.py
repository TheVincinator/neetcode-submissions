class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if prev[1] < intervals[i][0]:
                res.append(prev)
                prev = intervals[i]
                continue
            else:
                prev = [min(prev[0], intervals[i][0]), max(prev[1], intervals[i][1])]

        res.append(prev)
        return res