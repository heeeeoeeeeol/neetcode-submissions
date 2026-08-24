# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next        
            
        def reverseList(head):
            if not head or not head.next: return head
            nhead = reverseList(head.next)
            head.next.next = head
            head.next = None
            return nhead

        temp=slow.next 
        slow.next=None
        rev = reverseList(temp)

        def mergeTwoLists(list1, list2, isl1=True):
            if not list1:
                return list2
            elif not list2:
                return list1
            if isl1: 
                list1.next = mergeTwoLists(list1.next, list2, False)
                return list1
            else:
                list2.next = mergeTwoLists(list1, list2.next)
                return list2

        mergeTwoLists(head, rev)