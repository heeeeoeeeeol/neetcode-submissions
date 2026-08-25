# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            dummy = l = ListNode()

            while list1 and list2:
                if list1.val <= list2.val:
                    l.next = list1
                    list1 = list1.next
                    l = l.next
                else:
                    l.next = list2
                    list2 = list2.next
                    l = l.next

                l.next = list1 or list2

            return dummy.next


        if not lists: return None
        for i in range(1, len(lists)): 
            lists[0] = mergeTwoLists(lists[0], lists[i])
        return lists[0]


        