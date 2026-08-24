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
        dummy = Node(0, head)

        d = {None:None}

        while head:
            nhead = Node(head.val)
            d[head] = nhead
            head = head.next
            
        head = dummy.next
        while head:
            nhead = d[head]
            nhead.next = d[head.next]
            nhead.random = d[head.random]
            head = head.next

        return d[dummy.next]
            
            
