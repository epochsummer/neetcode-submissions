class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(0) # dummy
        self.tail = self.head
        self.size = 0

    
    def get(self, index: int) -> int:
        if self.size <=index:
            return -1
        node = self.head.next
        for i in range(index):
            node = node.next
        return node.value
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
            self.head.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
        self.size += 1
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
            self.head.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        if index == 0:
            self.head.next = self.head.next.next
        else:
            node = self.head
            for i in range(index):
                node = node.next
            if node.next == self.tail:
                node = self.tail
                node.next = None
            else:
                node.next = node.next.next

        self.size-= 1
        return True

    def getValues(self) -> List[int]:
        lst = []
        node = self.head
        for i in range(self.size):
            node = node.next
            lst.append(node.value)
        return lst

            

        
