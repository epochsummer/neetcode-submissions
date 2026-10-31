# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rounded = False
        dummy = ListNode()
        current = dummy
            

        list1 = l1
        list2 = l2


        while list1 != None and list2 != None:
            total = list1.val + list2.val
            if rounded:
                total += 1
            single_digit = total % 10
            new = ListNode(single_digit)
            current.next = new

            if total >= 10:
                rounded = True
            else:
                rounded = False

            list1 = list1.next
            list2 = list2.next
            current = current.next

        if list1 != None and list2 == None:
            while list1 != None:
                if rounded == True:
                    total = list1.val + 1
                else:
                    total = list1.val
                new = ListNode(total%10)
                current.next = new
                list1 = list1.next
                current = current.next
                if total >= 10:
                    rounded = True
                else: 
                    rounded = False

        elif list1 == None and list2 != None:
            while list2 != None:
                if rounded == True:
                    total = list2.val + 1
                else:
                    total = list2.val
                new = ListNode(total%10)
                current.next = new
                if total >= 10:
                    rounded = True
                else: 
                    rounded = False
                list2 = list2.next
                current = current.next
        
        if rounded == True:
            current.next = ListNode(1)
                
        return dummy.next
            

        
        