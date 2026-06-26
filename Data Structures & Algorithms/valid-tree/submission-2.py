class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for node, neigh in edges:
            adj_list[node].append(neigh)
            adj_list[neigh].append(node)

        visited = set()
        seen = set()
        def dfs(node, parent):
            if node in visited:
                return False
            if adj_list[node] == []:
                return True
            visited.add(node)
            for neigh in adj_list[node]:
                if neigh == parent:
                    continue
                if not dfs(neigh, node):
                    return False
            visited.remove(node)
            seen.add(node)
            adj_list[node] = []
            return True

        parent = None
        for node in range(n):
            if node in adj_list:
                if not dfs(node, parent):
                    return False
                break
        if len(seen) != len(adj_list):
            return False
        return True
