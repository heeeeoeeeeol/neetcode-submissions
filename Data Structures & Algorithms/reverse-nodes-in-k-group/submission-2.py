# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c = 0
        curr=head
        while curr and c < k:
            c+=1
            curr = curr.next
        if c < k: return head

        c = 0   
        tail=head
        prev = None
        while c < k:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
            c+=1

        tail.next = self.reverseKGroup(head, k)
        return prev


