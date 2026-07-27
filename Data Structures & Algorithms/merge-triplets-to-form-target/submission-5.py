class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [1, 1, 1]
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                res[0] = max(res[0], a)
                res[1] = max(res[1], b)
                res[2] = max(res[2], c)
                if target == res:
                    return True
        return False
            