class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        curr = 2
        for i in range(2, n + 1):
            prev, curr = curr, prev + curr
        return prev
        