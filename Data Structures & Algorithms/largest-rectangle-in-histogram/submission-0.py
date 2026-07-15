class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][0]:
                height, j = stack.pop()
                length = i - j
                res = max(res, height * length)
                start = j
            stack.append((heights[i], start))

        for height, i in stack:
            area = (len(heights) - i) * height
            res = max(res, area)
        return res