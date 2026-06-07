# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None or subRoot == None:
            return False
        
        #dfs call - check if subtrees are equal
        if self.dfs(root, subRoot) == True:
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        # self.isSubtree(root.left, subRoot.left)
        # self.isSubtree(root.right, subRoot.right)
        return left or right
            
      
    def dfs(self, root, subRoot):
        # if not root:
        #     return True
        if root == subRoot:
            return True
        if root and not subRoot:
            return False
        if not root and subRoot:
            return False
        if root.val != subRoot.val:
            return False
        return self.dfs(root.left, subRoot.left) and self.dfs(root.right, subRoot.right)