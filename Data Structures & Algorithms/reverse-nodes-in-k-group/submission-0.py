# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l = list(reversed(l[:k])) + l[k:] if len(l)-k<k else list(reversed(l[:k])) + list(reversed(l[k:]))

        dummy = lis = ListNode()

        for elem in l:
            lis.next = ListNode(elem)
            lis = lis.next

        return dummy.next