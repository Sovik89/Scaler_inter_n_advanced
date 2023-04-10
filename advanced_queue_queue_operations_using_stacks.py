from collections import deque

class UserQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main_stack=deque()
        self.dummmy_stack=deque()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.main_stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.dummmy_stack:
            return self.dummmy_stack.pop()
        else:
            while self.main_stack:
                self.dummmy_stack.append(self.main_stack.pop())
            
        return self.dummmy_stack.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.dummmy_stack:
            return self.dummmy_stack[-1]
        else:
            while self.main_stack:
                self.dummmy_stack.append(self.main_stack.pop())
        
        return self.dummmy_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.main_stack and not self.dummmy_stack:
            return True
        else:
            return False

# Your UserQueue object will be instantiated and called as such:
# obj = UserQueue()
# obj.push(x)
# param2 = obj.pop()
# param3 = obj.peek()
# param4 = obj.empty()