# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {}
        for i, node in enumerate(inorder):
            inorderMap[node] = i

        self.preorderIndex = 0
        def dfs(left, right):
            if left > right:
                return
            node = TreeNode(preorder[self.preorderIndex])
            mid = preorder[self.preorderIndex]
            self.preorderIndex += 1  
            node.left = dfs(left, inorderMap[mid] - 1)
            node.right = dfs(inorderMap[mid] + 1, right)
            return node

        return dfs(0, len(preorder) - 1)

        
        