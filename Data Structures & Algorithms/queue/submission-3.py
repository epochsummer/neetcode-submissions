class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.size == 0
        
    def append(self, value: int) -> None:
        node = Node(value)

        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node

        self.size += 1

    def appendleft(self, value: int) -> None:
        node = Node(value)

        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

        self.size += 1
        

    def pop(self) -> int:
        if self.size == 0:
            return -1
        popped = self.tail.prev.value

        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

        self.size -= 1
        return popped
        

    def popleft(self) -> int:
        if self.size == 0:
            return -1
        popped = self.head.next.value
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size-=1
        return popped
        
