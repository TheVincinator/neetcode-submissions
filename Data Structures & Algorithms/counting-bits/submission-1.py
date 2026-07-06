class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            x = 0
            while i != 0:
                x += i % 2
                i = i >> 1
            res.append(x)
        return res