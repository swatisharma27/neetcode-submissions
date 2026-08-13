"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        ## edge case
        if head is None:
            return None

        ## 1. Create a copy node and store next to original node
        curr = head
        while curr is not None:
            copyCurr = Node(curr.val)
            copyCurr.next = curr.next
            curr.next = copyCurr
            curr = curr.next.next

        ## 2. Handle random connections for new copy nodes
        curr = head
        copyCurr = head.next
        while curr is not None:
            if curr.random:
                copyCurr.random = curr.random.next
            curr = curr.next.next
            if copyCurr.next is not None:
                copyCurr = copyCurr.next.next

        ## 3. Separate original and copy LL
        curr = head
        copyCurr = head.next
        copyHead = head.next

        while curr is not None:
            curr.next = curr.next.next
            if copyCurr.next is not None:
                copyCurr.next = copyCurr.next.next
            curr = curr.next
            copyCurr = copyCurr.next

        return copyHead



        