import heapq

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n=len(A)
        if n==0:
            return 0
        if n==1:
            return A[0]
            
        #max heap
        max_heap=[]
        
        for i in range(n):
            heapq.heappush(max_heap,-A[i])
            
        
        while max_heap:
            y=-heapq.heappop(max_heap)
            if not max_heap:
                return y
            else:
                x=-heapq.heappop(max_heap)
                
            if y!=x:
                y=y-x
                if not max_heap:
                    return y
                else:
                    heapq.heappush(max_heap,-y)
            elif y==x:
                if not max_heap:
                    return 0