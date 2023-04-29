import heapq

def solve(A,B):

    
    n=len(B)
        
    min_heap=[]
    output_list=[]
    
    for i in range(n):
        heapq.heappush(min_heap,B[i])
        
        if i<A-1:
            output_list.append(-1)
            
        elif i==A-1:
            output_list.append(min_heap[0])
        else:
            heapq.heappop(min_heap)
            output_list.append(min_heap[0])
            
    return output_list