class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [1, 1, 1]
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            res = [max(res[0], a), max(res[1], b), max(res[2], c)]
            if target == res:
                return True
        return False
            