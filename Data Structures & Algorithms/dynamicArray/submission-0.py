class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size != self.capacity:
            self.arr[self.size] = n
        else:
            self.resize()
            self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        popping = self.arr[self.size-1]
        self.arr[self.size-1] = None
        self.size -= 1
        return popping
 

    def resize(self) -> None:
        new_arr = [None] * len(self.arr) * 2
        for i in range(len(self.arr)):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = len(new_arr)


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
