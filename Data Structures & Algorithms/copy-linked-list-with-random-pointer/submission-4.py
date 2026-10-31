"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        dictionary = {}

        current = dummy
        track = head

        while track != None:
            new = Node(track.val)
            current.next = new
            dictionary[track] = new

            current = current.next
            track = track.next
        
        current = dummy.next
        track = head

        while track != None:
            if track.random == None:
                current.random = None
            else:
                current.random = dictionary[track.random]

            current = current.next
            track = track.next
        
        return dummy.next

        