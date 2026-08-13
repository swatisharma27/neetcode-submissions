# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        ## 1. Find middle of LL
        slow = head
        fast = head
        ### ------ LL = even and LL = odd (considering both) ------ ###
        while fast.next != None and fast.next.next != None: 
            slow = slow.next
            fast = fast.next.next

        ## 2. Reverse second half of LL
        curr = slow.next
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        fast = prev

        ## 3. Break the connection after reversing
        slow.next = None

        ## 4. Merge the LLs
        slow = head

        while fast:
            temp = slow.next
            slow.next = fast
            temp2 = fast.next
            fast.next = temp
            slow = temp
            fast = temp2

        