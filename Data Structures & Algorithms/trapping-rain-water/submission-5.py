class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        totalArea = 0
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                totalArea += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                totalArea += maxRight - height[r]
        return totalArea
            