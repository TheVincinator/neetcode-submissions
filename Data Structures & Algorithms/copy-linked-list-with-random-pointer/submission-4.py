"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {}
        curr = head
        while curr:
            copy[curr] = Node(curr.val, None, None)
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                copy[curr].next = copy[curr.next]
            if curr.random:
                copy[curr].random = copy[curr.random]
            curr = curr.next

        return None if not head else copy[head]
        
        