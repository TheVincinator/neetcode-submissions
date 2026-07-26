class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.minimum:
            self.minimum.append(min(self.minimum[-1], value))
        else:
            self.minimum.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]