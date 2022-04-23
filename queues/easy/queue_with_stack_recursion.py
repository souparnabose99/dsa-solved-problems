

"""
@TODO:
Construct an algorithm to implement queues with the help of a stack.
O(N) additional memory usage allowed
"""


class Queue:

    def __init__(self):
        self.stack = []

    def enqueue(self, data):
        self.stack.append(data)

    # 2 stacks are used, 2nd stack is the call stack of memory
    def dequeue(self):
        if len(self.stack) == 1:
            return self.stack.pop()

        item = self.stack.pop()

        dequeued_item = self.dequeue()
        self.stack.append(item)

        return dequeued_item


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(30)
    queue.enqueue(19)
    queue.enqueue(79)
    print(queue.dequeue())
    print(queue.dequeue())
    # 10
    # 30

