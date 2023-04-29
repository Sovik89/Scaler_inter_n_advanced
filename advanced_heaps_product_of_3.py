import math,heapq

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n=len(A)
        
        #heapq.heapify(A)
        min_heap=[]
        output_list=[]
        
        for i in range(n):
            
            heapq.heappush(min_heap,A[i])
            
            if i<2:
                output_list.append(-1)
                
            elif i==2:
                output_list.append(math.prod(min_heap))
            else:
                heapq.heappop(min_heap)
                output_list.append(math.prod(min_heap))
                
        return output_list
        
