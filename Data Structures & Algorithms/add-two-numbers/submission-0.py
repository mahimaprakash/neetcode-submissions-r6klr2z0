# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        carry = 0

        while l1 and l2:
            nodeSum = (l1.val + l2.val) % 10
            carry +=  (l1.val + l2.val) // 10
            l2.val = nodeSum
            res.next = ListNode()
            res = res.next
            l1 = l1.next
            l2 = l2.next

        if carry:
            res.val = carry

        return dummy
