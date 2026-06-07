# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append((root, 0))
        d = {}
        while queue:
            node, level = queue.popleft()
            if node:
                d[level] = node.val
            if node:
                queue.append((node.left, level + 1))
            if node:
                queue.append((node.right, level + 1))
        result = []
        for n in range(len(d)):
            result.append(d[n])
        return result