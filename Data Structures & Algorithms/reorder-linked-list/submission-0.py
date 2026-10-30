# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        current = slow
        prev = None

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        terminal = prev

        list1 = head
        list2 = terminal
        dummy = ListNode()
        
        while list1 != slow:
            dummy.next = list1
            list1 = list1.next
            dummy = dummy.next

            dummy.next = list2
            list2 = list2.next
            dummy = dummy.next
        if list2 != None:
            dummy.next = list2
    



            
        
    

        



        