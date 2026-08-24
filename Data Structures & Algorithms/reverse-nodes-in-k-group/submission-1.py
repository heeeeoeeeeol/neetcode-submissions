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

        start = 0
        end = k
        rev = []
        while end <= len(l):
            rev += list(reversed(l[start:end]))
            start = end
            end += k 
        if end != len(l)+k:
            rev += l[start:]

        dummy = lis = ListNode()
        for elem in rev:
            lis.next = ListNode(elem)
            lis = lis.next
        return dummy.next