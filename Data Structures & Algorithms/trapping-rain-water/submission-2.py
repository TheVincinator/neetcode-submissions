class Solution:
    def trap(self, height: List[int]) -> int:
        totalArea = 0
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        maximum = 0
        for i in range(len(height)):
            maxLeft[i] = maximum
            maximum = max(maximum, height[i])
        maximum = 0
        for i in range(len(height) -1, -1, -1):
            maxRight[i] = maximum
            maximum = max(maximum, height[i])
        for i in range(len(height)):
            area = min(maxLeft[i], maxRight[i]) - height[i]
            if area > 0:
                totalArea += area
        return totalArea