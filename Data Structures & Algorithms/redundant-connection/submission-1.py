class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)

        visited = set()
        def dfs(prev, curr):
            if curr in visited:
                return True
            visited.add(curr)
            for neighbor in adj_list[curr]:
                if neighbor == prev:
                    continue
                if dfs(curr, neighbor):
                    return True
            return False

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
            visited = set()
            if dfs(None, n1):
                return [n1, n2]
        return []