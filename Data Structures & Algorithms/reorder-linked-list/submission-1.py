# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, node):
            prev = None
            curr = node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        
        ## 1. Middle of Linked List
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        ## 2. Reverse the second half
        fast = self.reverseList(slow.next)

        ## Disconnect to halves
        slow.next = None

        ## 3. Merge the two halves one node at a time
        slow = head
        while fast is not None:
            temp = slow.next
            slow.next = fast
            temp2 = fast.next
            fast.next = temp
            slow = temp
            fast = temp2


