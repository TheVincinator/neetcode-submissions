class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) space solution
        visited = set()
        for n in nums:
            if n in visited:
                return n
            visited.add(n)
        