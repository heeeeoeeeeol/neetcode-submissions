# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, list1, list2):
        dummy = l = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                l.next = list1
                list1 = list1.next
            else:
                l.next = list2
                list2 = list2.next
            l = l.next

        l.next = list1 or list2
        return dummy.next

    def divideList(self, lists):
        if len(lists) < 2: return lists[0]
        return self.mergeTwoLists(self.divideList(lists[:len(lists)//2]), self.divideList(lists[len(lists)//2:])) 

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        
        return self.divideList(lists)

        