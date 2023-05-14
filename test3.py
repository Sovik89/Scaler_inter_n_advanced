from collections import deque

def solve(A, B):
    
    #min_heap=[]
    my_queue=deque()
    
    for i in range(B):
        #heapq.heappush(min_heap,(i+1,0))
        my_queue.append((i+1,0))
        
    #print(min_heap)
    
    for row in A:
        first_flight,last_flight,allocated_seat=row
        i=1
        
        for j in range(B):
            current_flight,seats=my_queue.popleft()
            if first_flight<=current_flight<=last_flight:
                seats+=allocated_seat
            my_queue.append((current_flight,seats))
        
        # while stack:
        #     val=stack.pop()
        #     heapq.heappush(min_heap,val)
            
    output_list=[]
    
    while my_queue:        
        _,final_seat=my_queue.popleft()
        output_list.append(final_seat)
        
    
    return output_list    
    
    
    
            
    

print(solve([
    [1,2,10],
    [2,3,20],
    [2,5,25]
],5))