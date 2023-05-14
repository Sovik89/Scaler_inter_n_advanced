import heapq
from collections import deque

def solve(A, B):
    
    min_heap=[]
    stack=deque()
    
    for i in range(B):
        heapq.heappush(min_heap,(i+1,0))
        
    #print(min_heap)
    
    for row in A:
        first_flight,last_flight,allocated_seat=row
        i=1
        
        while i<=last_flight:
            current_flight,seats=heapq.heappop(min_heap)
            
            if first_flight<=current_flight<=last_flight:
                seats+=allocated_seat
            stack.append((current_flight,seats))
            i+=1
        
        while stack:
            val=stack.pop()
            heapq.heappush(min_heap,val)
            
    output_list=[]
    
    while min_heap:
        
        _,final_seat=heapq.heappop(min_heap)
        output_list.append(final_seat)
        
    
    return output_list    
    
    
    
            
    

print(solve([
    [1,2,10],
    [2,3,20],
    [2,5,25]
],5))
    
    
        
    
    
