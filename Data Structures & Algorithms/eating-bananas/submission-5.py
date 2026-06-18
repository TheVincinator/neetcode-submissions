class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            time = 0
            for num in piles:
                time += math.ceil(num / k)
            if time > h:
                l = k + 1
            else:
                res = k
                r = k - 1      
        return res