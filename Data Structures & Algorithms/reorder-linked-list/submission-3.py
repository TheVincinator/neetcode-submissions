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

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        curr1 = head
        curr2 = prev
        dummy = ListNode()
        while curr1 and curr2:
            dummy.next = curr1
            curr1 = curr1.next
            dummy = dummy.next
            dummy.next = curr2
            curr2 = curr2.next
            dummy = dummy.next
        
        if curr1:
            dummy.next = curr1
            curr1 = curr1.next
            dummy = dummy.next
        
        if curr2:
            dummy.next = curr2
            curr2 = curr2.next
            dummy = dummy.next

        