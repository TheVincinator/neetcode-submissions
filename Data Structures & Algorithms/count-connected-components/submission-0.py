class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor == prev:
                    continue
                dfs(neighbor, node)
            return

        result = 0
        for node in range(n):
            if node not in visited:
                dfs(node, None)
                result += 1
        return result