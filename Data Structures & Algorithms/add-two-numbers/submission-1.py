# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(l):
            prev = None
            while l:
                nxt = l.next
                l.next = prev
                prev = l
                l = nxt
            return prev
        revl1, revl2 = reverse(l1), reverse(l2)
        curr1, curr2 = revl1, revl2
        lst1, lst2 = [], []
        while curr1:
            lst1.append(str(curr1.val))
            curr1 = curr1.next
        while curr2:
            lst2.append(str(curr2.val))
            curr2 = curr2.next
        total = int("".join(lst1)) + int("".join(lst2))
        dummy = ListNode(0)
        tail = dummy
        for digit in str(total):
            tail.next = ListNode(int(digit))
            tail = tail.next
        return reverse(dummy.next)
        


