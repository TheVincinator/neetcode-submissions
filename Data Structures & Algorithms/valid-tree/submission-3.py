class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for node, neighbor in edges:
            adj_list[node].append(neighbor)
            adj_list[neighbor].append(node)

        visited = set()
        seen = set()
        def dfs(node, parent):
            if node in visited:
                return False
            if adj_list[node] == []:
                return True
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
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
