class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.prefix.append(min(self.minimum, val))
        self.minimum = min(self.minimum, val)

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.prefix = self.prefix[:-1]
        if self.prefix:
            self.minimum = self.prefix[-1]
        else:
            self.minimum = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]
