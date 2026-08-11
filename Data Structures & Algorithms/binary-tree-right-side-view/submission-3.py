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
        res = []
        prev_level = 0
        prev_node = root
        if not root:
            return res
        while queue:
            node, level = queue.popleft()
            if prev_level != level:
                res.append(prev_node.val)
            prev_level = level
            prev_node = node
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        res.append(prev_node.val)
        return res
            