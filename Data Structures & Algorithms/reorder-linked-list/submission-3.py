# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # after this slow will point to the head of second half

        # reverse second half
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # after this part, prev will point to the head of the second half which we just reversed
         
        # merge first and second half
        first = head
        second = prev

        while second:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            # first_next.next = second_next
            first, second = first_next, second_next