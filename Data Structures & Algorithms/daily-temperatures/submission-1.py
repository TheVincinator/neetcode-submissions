class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [(0, temperatures[0])]
        for j in range(1, len(temperatures)):
            while stack and stack[-1][1] < temperatures[j]:
                i, _ = stack.pop()
                res[i] = j - i
            stack.append((j, temperatures[j]))
        return res