# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, l1)
        while l1 and l2:
            l1.val = l1.val+l2.val
            if l1.val > 9:
                if l1.next: l1.next.val+=1
                elif l2.next: l2.next.val+=1 
                else: l1.next = ListNode(1)
                l1.val-=10
            l1=l1.next
            l2=l2.next

        if l2: l1=l2
        while l1:
            if l1.val > 9:
                if l1.next: l1.next.val+=1
                else: l1.next = ListNode(1)
                l1.val-=10
            l1=l1.next

        return dummy.next






