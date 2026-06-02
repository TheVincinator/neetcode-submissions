class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairList = []
        for i in range(len(position)):
            pairList.append([position[i], speed[i]])
        pairList.sort(reverse=True)
        stack = []
        for i in range(len(pairList)):
            time = (target - pairList[i][0]) / pairList[i][1]
            if stack and stack[-1] >= time:
                pass
            else:
                stack.append(time)
        return len(stack)


