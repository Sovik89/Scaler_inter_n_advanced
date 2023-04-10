from queue import Queue
from collections import deque

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        my_queue=Queue(0)

        #inserting all integers in a queue
        n=len(A)
        for i in range(n):
            my_queue.put(A[i])

        
        stacks=deque()

        for i in range(B):
            x=my_queue.get()
            stacks.append(x)

        while stacks:
            my_queue.put(stacks.pop())

        for i in range (n-B):
            x=my_queue.get()
            my_queue.put(x)

        A=[0]*n

        for i in range(n):
            A[i]=my_queue.get()

        
        return A