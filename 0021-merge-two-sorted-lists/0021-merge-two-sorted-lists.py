# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr_node = dummy
        i, j = list1, list2
        while i is not None and j is not None:
            if i.val <= j.val:
                curr_node.next = i
                i = i.next
            else:
                curr_node.next = j
                j = j.next
            curr_node = curr_node.next
        
        while i is not None:
            curr_node.next = i
            i = i.next
            curr_node = curr_node.next
        
        while j is not None:
            curr_node.next = j
            j = j.next
            curr_node = curr_node.next
            
        # the first node will have value 0, hence returning dummy.next
        return dummy.next