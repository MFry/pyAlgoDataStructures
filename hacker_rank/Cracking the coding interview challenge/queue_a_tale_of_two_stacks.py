from collections import deque


class MyQueue(object):
    def __init__(self):
        self.stack_in = deque()
        self.stack_out = deque()

    def peek(self):
        if len(self.stack_out) > 0:
            return self.stack_out[-1]
        else:
            return self.stack_in[0]

    def pop(self):
        if len(self.stack_out) == 0:
            for _ in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def put(self, value):
        self.stack_in.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
