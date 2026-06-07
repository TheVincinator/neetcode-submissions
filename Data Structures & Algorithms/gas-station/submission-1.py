class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        startIndex = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                startIndex = i + 1
                tank = 0
        return startIndex
            





            # lastIndex = i - 1
            # j = i + 1
            # if i == len(gas) - 1:
            #     j = 0
            # while totalTank > 0 and j != lastIndex:
            #     totalTank += gas[j] - cost[j]
            #     j = i + 1
            #     if i == len(gas) - 1:
            #         j = 0
            # print(i)
            # print("T: " + str(totalTank))
            # if totalTank >= 0 and j == lastIndex:
            #     return i
        # return -1