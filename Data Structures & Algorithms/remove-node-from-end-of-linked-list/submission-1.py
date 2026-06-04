# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        def reverse(head):
            prev = None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            return prev
        rev = ListNode(0, reverse(head))
        curr = rev
        i = 0
        while curr and i < n - 1:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return reverse(rev.next)