from math import inf

class MinStack:
    def __init__(self):
        self.min = inf
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self._setMin(val)

    def pop(self) -> None:
        self.stack.pop()
        self._nextMin()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

    def _setMin(self, val) -> None:
        self.min = min(self.min, val)
        self.mins.append(self.min)

    def _nextMin(self):
        self.mins.pop()

        if len(self.mins):
            self.min = self.mins[-1]
        else:
            self.min = inf

ms = MinStack()

# ["MinStack", "push", 0, "push", -1, "push", 0, "pop", "getMin", "pop", "getMin"]


ms.push(0)
ms.push(-1)
ms.push(0)
ms.pop()
print(ms.getMin())
ms.pop()
print(ms.getMin())
print('stack:', ms.stack)
print('mins:', ms.mins)
