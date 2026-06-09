# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maximum):
            if not root:
                return 0
            res = 1 if root.val >= maximum else 0
            maximum = max(maximum, root.val)
            res += dfs(root.left, maximum)
            res += dfs(root.right, maximum)
            return res
        return dfs(root, root.val)