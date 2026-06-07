# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        queue.append([root, 1])
        def bfs(root):
            prevLevel = 1
            level = []
            while queue:
                node, currLevel = queue.popleft()
                if prevLevel == currLevel:
                    level.append(node.val)
                elif currLevel > prevLevel:
                    result.append(level)
                    level = [node.val]
                if node.left:
                    queue.append([node.left, currLevel + 1])
                if node.right:
                    queue.append([node.right, currLevel + 1])
                prevLevel = currLevel
            result.append(level)
        if not root:
            return result
        bfs(root)
        return result
        
            

