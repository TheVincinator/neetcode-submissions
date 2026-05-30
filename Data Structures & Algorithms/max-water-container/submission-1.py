class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maximum = 0
        while i < j:
            lowestHeight = min(heights[i], heights[j])
            distance = j - i
            area = lowestHeight * distance
            maximum = max(maximum, area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maximum