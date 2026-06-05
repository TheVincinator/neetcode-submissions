# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        lst1, lst2 = [], []
        while curr1:
            lst1.append(str(curr1.val))
            curr1 = curr1.next
        while curr2:
            lst2.append(str(curr2.val))
            curr2 = curr2.next
        total = int(("".join(lst1))[::-1]) + int(("".join(lst2))[::-1])
        new = None
        for digit in str(total):
            new = ListNode(int(digit), new)
        return new
        


