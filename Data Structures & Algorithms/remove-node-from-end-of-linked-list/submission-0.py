# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = p2 = head
        c1, c2 = 0, 0
        
        while p1:
            p1=p1.next
            c1 += 1

        if c1 == n:
            head=head.next
            return head

        while c2 < c1-n-1:
            p2=p2.next
            c2 += 1

        if n==1:
            p2.next = None
            return head
        p2.next = p2.next.next
        return head

        
        
        