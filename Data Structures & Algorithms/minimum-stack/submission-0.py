class MinStack:

    def __init__(self):
        self.size = 0
        self.stack = []
        self.min_nums = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.size += 1
        if not self.min_nums or val <= self.min_nums[-1]:
            self.min_nums.append(val)
        else:
            self.min_nums.append(self.min_nums[-1])


    def pop(self) -> None:
        self.stack.pop(self.size-1)
        self.min_nums.pop()
        self.size -= 1

    def top(self) -> int:
        return self.stack[self.size - 1]
        

    def getMin(self) -> int:
        return self.min_nums[-1]
