
"""
@TODO:
Construct an algorithm to find the maximum item in a stick in O(1) runtime complexity.
O(N) additional memory usage allowed
"""


class MaxStack:

    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self, data):
        self.main_stack.append(data)

        if len(self.main_stack) == 1:
            self.max_stack.append(data)
            return

        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if self.size_of_stack() < 1:
            return
        data = self.main_stack[-1]
        del self.main_stack[-1]
        return data

    def peek(self):
        return self.main_stack[-1]

    def is_empty(self):
        return self.main_stack == []

    def size_of_stack(self):
        return len(self.main_stack)

    def pop_max_item(self):
        return self.max_stack[-1]

    def get_max_item(self):
        return self.pop_max_item()


stack = MaxStack()
stack.push(26)
stack.push(57)
stack.push(903)
stack.push(105)
print("Size of stack : ", stack.size_of_stack())
print("Max item in stack : ", stack.get_max_item())


