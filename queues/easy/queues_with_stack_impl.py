

"""
@TODO:
Construct an algorithm to implement queues with the help of a stack.
O(N) additional memory usage allowed
"""


class Queue:

    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception("No data present in stacks....")

        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()


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

