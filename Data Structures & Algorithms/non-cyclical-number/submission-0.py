class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            sum_squares = 0
            for c in str(n):
                sum_squares += int(c) * int(c)
            if sum_squares == 1:
                return True
            n = sum_squares
        return False
            
        