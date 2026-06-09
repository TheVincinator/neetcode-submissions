# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        def dfs(root, maximum):
            if not root:
                return
            if root.val >= maximum:
                maximum = root.val
                count[0] += 1
            dfs(root.left, maximum)
            dfs(root.right, maximum)
        dfs(root, root.val)
        return count[0]