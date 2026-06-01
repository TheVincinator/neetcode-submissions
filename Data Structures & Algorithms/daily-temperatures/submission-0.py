class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, j = stack.pop()
                result[j] = i - j
            stack.append((t,i))
        return result