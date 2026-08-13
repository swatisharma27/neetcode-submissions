# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while fast != None and fast.next != None:

            slow = slow.next ## 1X times
            fast = fast.next.next ## 2X times

            if slow == fast:
                slow = head
                while fast != None and fast.next != None:

                    slow = slow.next ## 1X times
                    fast = fast.next ## 2X times
                    if slow == fast:
                        index = slow
                        return True
        return False
                

                    
        