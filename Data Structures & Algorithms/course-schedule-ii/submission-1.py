class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for c, p in prerequisites:
            adj_list[c].append(p)

        result = []
        visited = set()
        cycle = set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for prerequisite in adj_list[course]:
                if not dfs(prerequisite):
                    return False
            cycle.remove(course)
            visited.add(course)
            result.append(course)
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return []
        return result