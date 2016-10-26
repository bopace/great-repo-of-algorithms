# Bo Pace, Oct 2016
# Stack
# Implementation using the built-in list. Really, Python lists
# have the right built-in operations that making your own
# stack class is a bit redundant, but it's a good exercise
# anyhow. I'll be implementing the push, pop, peek, empty, and
# size operations.

class stack:
    def __init__(self):
        self.container = []

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.container)
