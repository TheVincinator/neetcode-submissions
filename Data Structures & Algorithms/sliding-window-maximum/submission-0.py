class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        i = 0
        j = 0
        while j < k:
            count[nums[j]] += 1
            j += 1

        res = []
        while j < len(nums):
            res.append(max(count.keys()))
            count[nums[i]] -= 1
            if count[nums[i]] == 0:
                del count[nums[i]]
            i += 1
            count[nums[j]] += 1
            j += 1
        res.append(max(count.keys()))

        return res

        