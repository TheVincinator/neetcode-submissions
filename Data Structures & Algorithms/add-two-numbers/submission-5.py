# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            if total >= 10:
                carry = total // 10
                total = total % 10
            else:
                carry = 0
            curr.next = ListNode(total)
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        while l1:
            total = l1.val + carry
            carry = total // 10
            total = total % 10
            curr.next = ListNode(total)
            l1 = l1.next
            curr = curr.next
        while l2:
            total = l2.val + carry
            carry = total // 10
            total = total % 10
            curr.next = ListNode(total)
            l2 = l2.next
            curr = curr.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next

