class Solution:
    def myPow(self, x: float, n: int) -> float:
        def myPowRec(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n % 2 == 1:
                return x * myPowRec(x, n // 2) * myPowRec(x, n // 2)
            return myPowRec(x, n // 2) * myPowRec(x, n // 2)

        res = myPowRec(x, abs(n))
        return 1 / res if n < 0 else res
        
