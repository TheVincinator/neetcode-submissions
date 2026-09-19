# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {}
        for i, value in enumerate(inorder):
            inorderMap[value] = i

        self.preorderIndex = 0
        def dfs(left, right):
            if left > right:
                return
            node = TreeNode(preorder[self.preorderIndex])
            mid = inorderMap[preorder[self.preorderIndex]]
            self.preorderIndex += 1
            node.left = dfs(left, mid - 1)
            node.right = dfs(mid + 1, right)
            return node

        return dfs(0, len(inorder) - 1)

        
        