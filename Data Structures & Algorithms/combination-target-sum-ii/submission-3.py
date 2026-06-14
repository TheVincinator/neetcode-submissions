class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def dfs(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop()
            distinct = candidates[i]
            while i + 1 < len(candidates) and candidates[i + 1] == distinct:
                i += 1
            dfs(i + 1, curr, total)
        dfs(0, [], 0)
        return result