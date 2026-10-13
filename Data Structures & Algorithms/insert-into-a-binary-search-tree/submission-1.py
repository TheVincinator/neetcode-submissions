# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def dfs(node):
            if val < node.val and node.left:
                node.left = self.insertIntoBST(node.left, val)
            elif val > node.val and node.right:
                node.right = self.insertIntoBST(node.right, val)
            elif val < node.val and not node.left:
                node.left = TreeNode(val)
            else:
                node.right = TreeNode(val)

        dfs(root)
        return root
