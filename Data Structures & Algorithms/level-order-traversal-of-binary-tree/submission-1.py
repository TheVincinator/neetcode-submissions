# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append((root, 0))
        res = []
        sub = []
        prev_level = 0
        if not root:
            return res
        while queue:
            node, level = queue.popleft()
            if prev_level != level:
                res.append(sub)
                sub = []
            sub.append(node.val)
            prev_level = level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        res.append(sub)
        return res
            
            
        
            

