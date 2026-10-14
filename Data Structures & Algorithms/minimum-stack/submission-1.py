class MinStack:

    def __init__(self):
        self.array = []
        self.smallest = []
        

    def push(self, val: int) -> None:
        if len(self.array) == 0 or self.smallest[-1] >= val:
            self.smallest.append(val)
        self.array.append(val)

    def pop(self) -> None:
        if self.array[-1] == self.smallest[-1]:
            self.smallest.pop()
        self.array.pop()

    def top(self) -> int:
        return self.array[-1]
        

    def getMin(self) -> int:
        return self.smallest[-1]
        
