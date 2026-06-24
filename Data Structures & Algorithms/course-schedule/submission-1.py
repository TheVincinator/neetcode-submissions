class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for c, p in prerequisites:
            adj_list[c].append(p)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if adj_list[course] == []:
                return True
            visited.add(course)
            for prerequisite in adj_list[course]:
                if not dfs(prerequisite):
                    return False
            visited.remove(course)
            adj_list[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True