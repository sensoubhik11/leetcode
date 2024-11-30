# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge_util(list1, list2):
            if list1.next is None:
                list1.next = list2
                return list1
            curr1, next1 = list1, list1.next
            curr2, next2 = list2, list2.next

            while next1 and curr2:
                if curr2.val >= curr1.val and curr2.val <= next1.val:
                    next2 = curr2.next
                    curr1.next = curr2
                    curr2.next = next1
                    
                    curr1 = curr2
                    curr2 = next2
                else:
                    curr1 = next1
                    next1 = curr1.next
            if curr2 is not None:
                curr1.next = curr2
            return list1
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            return merge_util(list1, list2)
        else:
            return merge_util(list2, list1)

                    
