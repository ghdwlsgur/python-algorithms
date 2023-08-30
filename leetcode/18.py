
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.pointer = -1

    def push(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.stack.append(val)
        self.pointer += 1

    def pop(self):
        """
        :rtype: int
        """
        if self.pointer > -1:
            self.stack.pop()
            self.pointer -= 1

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.pointer] if self.pointer > -1 else None

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack) if self.pointer > -1 else None

min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())
min_stack.pop()
print(min_stack.top())
print(min_stack.getMin())

