# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        if not root:
            return 0
        self.diameter = max(self.diameter, height(root.left) + height(root.right))
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return self.diameter

