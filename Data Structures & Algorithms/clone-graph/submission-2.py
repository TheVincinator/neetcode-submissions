"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}
        if not node:
            return None
        def clone(node):
            if node not in nodeMap:
                nodeMap[node] = Node(node.val)
            else:
                return nodeMap[node]
            for neighbor in node.neighbors:
                if neighbor in nodeMap:
                    nodeMap[node].neighbors.append(nodeMap[neighbor])
                else:
                    nodeMap[node].neighbors.append(clone(neighbor))
            return nodeMap[node]
        return clone(node)