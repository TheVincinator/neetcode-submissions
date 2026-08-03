class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        res = max(piles)
        while i <= j:
            k = (i + j) // 2
            time = 0
            for num in piles:
                time += math.ceil(num / k)
            if time > h:
                i = k + 1
            elif time <= h:
                res = k
                j = k - 1
            else:
                return k
        return res
            