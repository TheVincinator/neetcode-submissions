# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        prev = None
        curr = head2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        curr1 = head
        curr2 = prev
        dummy = ListNode()
        tail = dummy
        while curr1 and curr2:
            nxt1 = curr1.next
            nxt2 = curr2.next
            tail.next = curr1
            tail = tail.next
            tail.next = curr2
            tail = tail.next
            curr1 = nxt1
            curr2 = nxt2
        if curr1:
            tail.next = curr1
        else:
            tail.next = curr2

        head = dummy.next
        
        