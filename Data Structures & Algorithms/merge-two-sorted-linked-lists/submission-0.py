# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2

        if list1 == None:
            return list2
        if list2 == None:
            return list1

        if list1.val >= list2.val:
            head = list2
            current2 = current2.next
        else:
            head = list1
            current1 = current1.next

        current_node = head
        
        while current1 and current2:
            if current1.val > current2.val:
                current_node.next = current2
                current2 = current2.next
            else:
                current_node.next = current1
                current1 = current1.next
            current_node = current_node.next
        
        if current1 == None:
            current_node.next = current2
        else:
            current_node.next = current1
        return head


        