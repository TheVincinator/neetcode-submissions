"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        ref = {}
        def cloneGraphRec(node):
            if not node:
                return None
            if node in ref:
                return ref[node]
            ref[node] = Node(node.val)
            for n in node.neighbors:
                cloned_neighbor = cloneGraphRec(n)
                ref[node].neighbors.append(cloned_neighbor)
            return ref[node]
        return cloneGraphRec(node)