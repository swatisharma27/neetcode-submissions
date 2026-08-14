# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(val = -1, next = head)
        start = dummy
        curr = head
        count = 0

        while curr is not None:

            curr = curr.next
            count += 1

            if count % k == 0:
                start = self.reverse(start, curr)

        return dummy.next
        
    def reverse(self, start, end):

        prev = None
        curr = start.next
        first = start.next

        while curr != end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        start.next = prev
        first.next = end

        return first

        