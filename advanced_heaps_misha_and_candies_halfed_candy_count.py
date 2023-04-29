import heapq


def solve(A, B):
    #min_heap=[]
    
    heapq.heapify(A)
    
    answer=0
    while A:
        popped_val=heapq.heappop(A)
        
        if popped_val>B:
            break
        
        half_popped_val=popped_val//2
        
        answer+=half_popped_val
        
        if A:
            updated_box=heapq.heappop(A)
            updated_box=updated_box+(popped_val-half_popped_val)
            heapq.heappush(A,updated_box)
        
    return answer
    

    

print(solve([795],867))
    