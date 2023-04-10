from collections import deque

class MinStack:       
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stacks.append(x)
        if not self.min_stack or x<=self.min_stack[-1]:
            self.min_stack.append(x)        

        

    # @return nothing
    def pop(self):
        if self.stacks:
            if self.stacks.pop() == self.min_stack[-1]:
                return self.min_stack.pop()
        

    # @return an integer
    def top(self):
        if self.stacks:
            return self.stacks[-1]
        else:
            return -1
        

    # @return an integer
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return -1
        
    
    def __init__(self):
        self.stacks=deque()
        self.min_stack=deque()