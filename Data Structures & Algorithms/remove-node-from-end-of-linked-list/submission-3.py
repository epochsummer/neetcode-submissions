# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        current = head

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        tail = prev
        dummy = ListNode()   
        dummy.next = tail
        current = dummy
        index = 0

        while index != n:
            if index + 1 == n:
                remove = current.next
                current.next = current.next.next
                if remove == tail:
                    tail = current.next
                remove.next = None
                break
                
            else:
                current = current.next
                index += 1
        
        current = tail
        prev = None
        

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

        