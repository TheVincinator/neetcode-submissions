class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow():
            res = 1
            for _ in range(abs(n)):
                res *= x
            return res

        if n < 0:
            return 1 / pow()
        else:
            return pow()