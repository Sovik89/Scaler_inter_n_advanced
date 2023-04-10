#import queue
from collections import deque

class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        #my_queue=queue.Queue()
        my_deque=deque()
    
        output_list=[]
        
        # my_queue.put(1)
        # my_queue.put(2)
        # my_queue.put(3)
        my_deque.append(1)
        my_deque.append(2)
        my_deque.append(3)
        
        for i in range(A):
            #x=my_queue.get()
            x=my_deque.popleft()
            output_list.append(x)
            for j in range(1,4):
                my_deque.append((10*x)+j)
            
        return output_list


print(solve(2))
        