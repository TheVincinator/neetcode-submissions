class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for node, neigh in edges:
            adj_list[node].append(neigh)
            adj_list[neigh].append(node)

        visited = set()
        h = set()
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
            h.add(node)
            adj_list[node] = []
            return True

        parent = None
        checked = False
        for node in range(n):
            if checked and len(h) != len(adj_list):
                return False
            elif node in adj_list:
                if not dfs(node, parent):
                    return False
                checked = True
        return True
