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
        copy = Node(0, None, None)
        tail = copy
        curr = head
        while curr:
            tail.next = Node(curr.val, None, None)
            tail = tail.next
            curr = curr.next

        d = {}
        tail = copy.next
        curr = head
        while curr:
            d[curr] = tail
            tail = tail.next
            curr = curr.next
    
        tail = copy.next
        curr = head
        while curr:
            if not curr.random:
                tail.random = None
            else:
                tail.random = d[curr.random]
            tail = tail.next
            curr = curr.next
        
        return copy.next
        